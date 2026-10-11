
import streamlit as st
import numpy as np
import joblib

st.set_page_config(
    page_title="Electrical Fault Detection",
    page_icon="⚡",
    layout="wide"
)

st.title("Electrical Fault Detection System")
st.write(
    "Enter three-phase currents and voltages to compare "
    "the predictions from two trained classifiers."
)

# Load saved models and training statistics
theta_Q = np.load("theta_Q.npy")
stats_Q = np.load("scaling_stats_Q.npz")

mean_Q = stats_Q["mean"]
std_Q = stats_Q["std"]

stats_R = np.load("scaling_stats.npz")
mean_R = stats_R["mean"]
std_R = stats_R["std"]

saved_R = joblib.load("best_rbf_svm.joblib")

if isinstance(saved_R, dict):
    rbf_model = next(
        (
            value
            for value in saved_R.values()
            if callable(getattr(value, "predict", None))
        ),
        None,
    )

    if rbf_model is None:
        st.error(
            "No trained model found in the saved dictionary. "
            f"Available keys: {list(saved_R.keys())}"
        )
        st.stop()
else:
    rbf_model = saved_R

st.subheader("Electrical measurements")

with st.form("measurements"):
    col1, col2, col3 = st.columns(3)

    with col1:
        Ia = st.number_input("Ia (A)", value=0.0)
        Ib = st.number_input("Ib (A)", value=0.0)

    with col2:
        Ic = st.number_input("Ic (A)", value=0.0)
        Va = st.number_input("Va (p.u.)", value=1.0)

    with col3:
        Vb = st.number_input("Vb (p.u.)", value=-0.5)
        Vc = st.number_input("Vc (p.u.)", value=-0.5)

    submitted = st.form_submit_button("Detect fault")

if submitted:
    # Six raw measurements
    raw = np.array(
        [[Ia, Ib, Ic, Va, Vb, Vc]],
        dtype=float
    )

    # Set Q: squares are calculated before standardisation
    raw_Q = np.column_stack([raw, raw ** 2])
    scaled_Q = (raw_Q - mean_Q) / std_Q

    # Add intercept for logistic regression
    X_Q = np.column_stack([
        np.ones(len(scaled_Q)),
        scaled_Q
    ])

    probability = 1 / (
        1 + np.exp(-np.clip(X_Q @ theta_Q, -500, 500))
    )

    logistic_prediction = int(probability[0] >= 0.5)

    # Set R: standardise the six measurements
    scaled_R = (raw - mean_R) / std_R
    rbf_prediction = int(rbf_model.predict(scaled_R)[0])

    st.subheader("Prediction results")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Set Q Logistic Regression")

        if logistic_prediction == 1:
            st.error("Fault detected")
        else:
            st.success("No fault detected")

        fault_probability = float(np.asarray(probability).ravel()[0])

    st.write(
    f"Estimated fault probability: {fault_probability:.2%}"
)

    with col2:
        st.markdown("### RBF Support Vector Machine")

        if rbf_prediction == 1:
            st.error("Fault detected")
        else:
            st.success("No fault detected")

    if logistic_prediction != rbf_prediction:
        st.warning(
            "The models disagree. Further assessment is required."
        )

st.caption(
    "Educational prototype only. This application is not "
    "a certified protection relay and must not control "
    "real electrical equipment."
)