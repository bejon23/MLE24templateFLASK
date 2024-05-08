import os
import sys
print(sys.executable)

import numpy as np

from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open("D:/template/svm_clf.pkl", "rb"))


# Set the template folder path
template_folder = os.path.join("D:/", "template", "templates")
app.template_folder = template_folder

# Set the static folder path
static_folder = os.path.join("D:/", "template", "static")
app.static_folder = static_folder


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










