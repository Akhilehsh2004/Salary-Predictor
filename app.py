import pickle
import numpy as np
from flask import Flask, render_template, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Load trained model
with open('salary.pkl', 'rb') as file:
    model = pickle.load(file)

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction Route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user input from the form
        experience = float(request.form['experience'])

        # Convert to 2D array for model prediction
        prediction = model.predict(np.array([[experience]]))[0]

        return jsonify({'salary': f"₹{prediction:,.2f}"})
    except Exception as e:
        return jsonify({'error': str(e)})

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)
