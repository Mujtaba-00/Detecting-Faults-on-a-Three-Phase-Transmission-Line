⚡ Detecting Faults on a Three-Phase Transmission Line
📌 Overview
Electrical Fault Detection Using Machine Learning is a machine learning project designed to identify and classify electrical faults using electrical system data. The project applies machine learning algorithms to analyse input parameters and predict the type of fault, helping improve electrical system monitoring, protection, and reliability.

The project explores different machine learning models and compares their performance using standard evaluation metrics.

🎯 Objectives
Detect electrical faults using machine learning techniques.
Classify electrical system conditions based on input features.
Train and evaluate multiple machine learning models.
Compare model performance using suitable evaluation metrics.
Develop a prediction system that can classify new electrical data.
Explore how machine learning can support electrical system protection and monitoring.
🚀 Features
Electrical fault classification and prediction.
Data preprocessing and feature scaling.
Training and testing of machine learning models.
Model performance evaluation.
Comparison of different classification algorithms.
Prediction of electrical faults using new input data.
Visualisation of model performance and results.
🧠 Machine Learning Models
The project can include the following algorithms, depending on the models implemented in the code:

Logistic Regression: Classifies electrical conditions using a linear decision boundary.
Support Vector Machine (SVM): Separates different fault classes using an optimal decision boundary.
Random Forest: Combines multiple decision trees to improve classification performance.
RBF-based Classifier: Uses a Radial Basis Function to model nonlinear relationships between input features and fault classes.
Each model can be evaluated to determine which performs best on the selected dataset.

🛠️ Technologies Used
Programming Language: Python
Data Processing: Pandas, NumPy
Machine Learning: Scikit-learn
Data Visualisation: Matplotlib, Seaborn
Development Environment: Jupyter Notebook / VS Code
Model Persistence: Pickle or Joblib, if used in the implementation
📊 Model Evaluation
The trained models can be evaluated using the following metrics:

Metric	Purpose
Accuracy	Measures the proportion of correct predictions.
Precision	Measures how many predicted faults of a class are correct.
Recall	Measures how many actual faults of a class are detected.
F1-Score	Balances precision and recall.
Confusion Matrix	Shows correct and incorrect predictions for each class.
For electrical fault detection, recall is particularly important because missed fault conditions may create safety and equipment risks. Precision should also be considered to reduce false alarms.

Actual evaluation results should be added after running the models on the test dataset.

🔍 How It Works
Data Collection: Load the electrical fault dataset.
Data Preprocessing: Clean the data and prepare the input features.
Feature Preparation: Separate input variables from the target fault labels.
Data Splitting: Divide the dataset into training and testing sets.
Model Training: Train the selected machine learning algorithms.
Model Evaluation: Compare predictions against the actual labels.
Fault Prediction: Use a trained model to classify new electrical measurements.
Result Display: Present the predicted fault class and relevant evaluation results.
💡 Applications
Electrical power system monitoring.
Fault classification in transmission and distribution networks.
Electrical equipment protection research.
Industrial electrical system diagnostics.
Smart grid monitoring and analysis.
Machine learning applications in power system engineering.
⚠️ Limitations
Prediction performance depends on the quality and representativeness of the dataset.
Unseen fault conditions may not be classified reliably.
Real-time deployment requires appropriate sensors, data acquisition, and system integration.
The model should not replace certified electrical protection systems without extensive validation and safety testing.
🔮 Future Improvements
Integrate real-time electrical measurements from sensors.
Develop a live monitoring dashboard.
Add more fault types and operating conditions.
Compare additional machine learning and deep learning models.
Implement fault alerts and data logging.
Test the model using real-world electrical system data.
👨‍💻 Author
Muhammad Mujtaba

Electrical Engineering | Electronics Engineering

📜 License
This project is intended for educational and research purposes. Add an appropriate open-source license, such as the MIT License, if you want others to reuse and modify the code.

⭐ If you find this project useful, consider giving the repository a star!
