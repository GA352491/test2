from flask import Flask
import json
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    df = pd.read_json('src/details.json')
    ls = []
    for data in df['HeightCm']:
        ls.append(int(data) / 100)

    df['HeightCm'] = ls

    df['BMI'] = df['WeightKg'] / (df['HeightCm'] ** 2)
    print(df)
    category = []
    risk = []

    for bmi in df['BMI']:
        if round(bmi, 1) <= 18.4:
            category.append('Underweight')
            risk.append('Malnutrition risk')
        elif round(bmi, 1) > 18.5 and round(bmi, 1) < 24.9:
            category.append('Normal weight')
            risk.append('Low risk')
        elif round(bmi, 1) > 25 and round(bmi, 1) < 29.9:
            category.append('Overweight')
            risk.append('Enhanced risk')
        elif round(bmi, 1) > 30 and round(bmi, 1) < 34.9:
            category.append('Moderately obese')
            risk.append('Medium risk')
        elif round(bmi, 1) > 35 and round(bmi, 1) < 39.9:
            category.append('Severely obese')
            risk.append('High risk')
        elif round(bmi, 1) >= 40:
            category.append('Very severely obese')
            risk.append('Very high risk')
    df['category'] = category
    df['risk'] = risk
    # print(df)
    overweight_count = df.value_counts('category')['Overweight']
    print("total no of overweight count in give data are :" + str(overweight_count))
    return df, overweight_count



if '__name__' == 'main':
    app.run()
