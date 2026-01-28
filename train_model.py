
import kagglehub
import pandas as pd
import numpy as np
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

def train():
    print("Downloading dataset...")
    # Download the dataset from KaggleHub
    path = kagglehub.dataset_download("mabubakrsiddiq/student-exam-performance")
    print("Dataset downloaded to:", path)

    # Load the dataset
    files = os.listdir(path)
    file_path = os.path.join(path, files[0])
    data = pd.read_csv(file_path)

    # Drop irrelevant columns
    if "motivation_score" in data.columns:
        data = data.drop(["motivation_score", "exam_anxiety_score"], axis=1)

    # Feature Engineering
    data["average_prev_score"] = (
        data["math_prev_score"] +
        data["science_prev_score"] +
        data["language_prev_score"]
    ) / 3

    data["pass"] = data["average_prev_score"].apply(lambda x: 1 if x >= 50 else 0)

    # Label Encoding with separate encoders for each column
    encoders = {}
    for col in data.columns:
        if data[col].dtype == "object":
            le = LabelEncoder()
            data[col] = le.fit_transform(data[col])
            encoders[col] = le
    
    # Define features and target
    X = data.drop(["pass", "average_prev_score"], axis=1)
    y = data["pass"]

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    print("Training model...")
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred))

    # Save model and encoders
    joblib.dump(model, "model.pkl")
    joblib.dump(encoders, "encoders.pkl")
    print("Model and encoders saved to 'model.pkl' and 'encoders.pkl'")

if __name__ == "__main__":
    train()
