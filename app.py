import os
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import requests

app = Flask(__name__)

# Download the model file from GitHub repository
model_url = "https://github.com/ronysaimon16/MLE24templateFLASK/raw/main/svm_clf.pkl"
model_file = os.path.join(app.root_path, "svm_clf.pkl")
response = requests.get(model_url)
with open(model_file, "wb") as f:
    f.write(response.content)

# Load the model
model = pickle.load(open(model_file, "rb"))

# Set the template folder path
app.template_folder = os.path.join(app.root_path, "templates")

# Set the static folder path
app.static_folder = os.path.join(app.root_path, "static")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Get feature values from the form
    bmi = float(request.form['BMI'])
    smoking = request.form['Smoking']
    alcohol_drinking = request.form['AlcoholDrinking']
    stroke = request.form['Stroke']
    physical_health = float(request.form['PhysicalHealth'])
    mental_health = float(request.form['MentalHealth'])
    diff_walking = request.form['DiffWalking']
    sex = request.form['Sex']
    age_category = request.form['AgeCategory']
    race = request.form['Race']
    diabetic = request.form['Diabetic']
    physical_activity = request.form['PhysicalActivity']
    gen_health = request.form['GenHealth']
    sleep_time = float(request.form['SleepTime'])
    asthma = request.form['Asthma']
    kidney_disease = request.form['KidneyDisease']
    skin_cancer = request.form['SkinCancer']

    # Make prediction
    prediction = model.predict([[bmi, smoking, alcohol_drinking, stroke, physical_health, mental_health, diff_walking, sex, age_category, race, diabetic, physical_activity, gen_health, sleep_time, asthma, kidney_disease, skin_cancer]])[0]

    # Render the result template with the prediction
    return render_template('result.html', prediction=prediction)


if __name__ == "__main__":
    # Get the port number from the environment variable PORT or use 4000 as fallback
    port = int(os.environ.get("PORT", 4000))
    app.run(host='0.0.0.0', port=port)
