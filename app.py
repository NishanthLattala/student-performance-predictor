
from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load model and encoders
try:
    model = joblib.load("model.pkl")
    encoders = joblib.load("encoders.pkl")
    print("Model and encoders loaded successfully.")
except Exception as e:
    print(f"Error loading model/encoders: {e}")
    model = None
    encoders = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if not model or not encoders:
        return jsonify({"error": "Model not loaded. Please run train_model.py first."}), 500

    try:
        # Get data from form
        data = request.form.to_dict()
        
        # Prepare input DataFrame with correct column order
        # We need to reconstruct the dataframe with the exact columns used during training
        # Based on the notebooks logic, the columns in X were:
        # student_id, final_score, grade, pass_fail, previous_score, math_prev_score, 
        # science_prev_score, language_prev_score, daily_study_hours, attendance_percentage, 
        # homework_completion_rate, sleep_hours, screen_time_hours, physical_activity_minutes, 
        # parent_education_level, study_environment
        
        # NOTE: In a real scenario, passing 'final_score', 'grade', and 'pass_fail' (original) 
        # as inputs to predict 'pass' (calculated from avg_prev_score) is unusual data leakage, 
        # but I am strictly following the user's provided logic which included them in X.
        
        input_data = {}
        
        # Helper to safely parse numbers
        def parse_float(val):
            try:
                return float(val)
            except:
                return 0.0

        # Helper to encode categorical variables
        def encode(col, val):
            if col in encoders:
                try:
                    return encoders[col].transform([val])[0]
                except ValueError:
                    # Handle unseen labels by assigning a default or the first class
                    return encoders[col].transform([encoders[col].classes_[0]])[0]
            return val

        # We need to map form fields to model columns.
        # Assuming the form sends the exact names.
        
        # For simplicity in this demo, I will hardcode keys or assume they exist in the form.
        # Ideally, we should validate this.
        
        # List of expected columns in order (reconstructed from training logic)
        expected_columns = [
            'student_id', 'final_score', 'grade', 'pass_fail', 'previous_score',
            'math_prev_score', 'science_prev_score', 'language_prev_score',
            'daily_study_hours', 'attendance_percentage', 'homework_completion_rate',
            'sleep_hours', 'screen_time_hours', 'physical_activity_minutes',
            'parent_education_level', 'study_environment'
        ]
        
        processed_input = []
        
        for col in expected_columns:
            val = data.get(col)
            
            # If value is missing, use a default (0 or calculated mean could be better)
            if val is None:
                # For string cols, use empty string? Or handle specific defaults
                if col in encoders:
                     val = encoders[col].classes_[0] # Default to first class
                else:
                    val = 0.0

            if col in encoders:
                 processed_input.append(encode(col, val))
            else:
                 processed_input.append(parse_float(val))

        # Create DataFrame for prediction (reshape to 2D)
        # input_df = pd.DataFrame([processed_input], columns=expected_columns) 
        # The model just needs a numpy array or similar-structured list
        prediction = model.predict([processed_input])

        result = "PASS" if prediction[0] == 1 else "FAIL"
        
        return render_template("index.html", prediction_text=f"Student will {result}")

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
