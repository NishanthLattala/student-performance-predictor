Student Performance Predictor
This project aims to predict student performance (pass/fail) based on various academic and environmental factors. By leveraging machine learning, it identifies key indicators that influence a student's success.

Project Overview:

Objective: To build a predictive model that can forecast whether a student will pass or fail, providing insights into influential factors.
Dataset: The project utilizes the 'Student Exam Performance' dataset from KaggleHub, which includes student IDs, scores in different subjects, study habits, attendance, and environmental factors.
Methodology:
    Data Preparation: The initial raw data is cleaned by removing irrelevant columns and engineering new features like 'average_prev_score'.
    Feature Encoding: Categorical variables such as parent education level and study environment are transformed into numerical formats using Label Encoding.
    Model Training: A Logistic Regression model is trained on the processed data to learn the patterns associated with student performance.
    Evaluation: The model's effectiveness is assessed using accuracy and a classification report to understand its ability to correctly predict pass/fail outcomes.
Outcome: The trained model provides predictions for individual students, indicating their likelihood of passing, which can be valuable for early intervention and support.
