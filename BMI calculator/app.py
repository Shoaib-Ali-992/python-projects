from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(weight_kg, height_m):
    """
    Function to calculate BMI.
    Formula: BMI = weight (kg) / (height (m) ** 2)
    """
    bmi = weight_kg / (height_m ** 2)
    return bmi

def interpret_bmi(bmi, gender, age):
    """
    Function to interpret BMI and provide a classification based on gender and age.
    """
    if gender == 'male':
        if age < 18:
            if bmi < 16:
                return "Severely underweight"
            elif 16 <= bmi < 17:
                return "Underweight"
            elif 17 <= bmi < 23:
                return "Normal weight"
            elif 23 <= bmi < 25:
                return "Overweight"
            else:
                return "Obese"
        else:
            if bmi < 18.5:
                return "Underweight"
            elif 18.5 <= bmi < 25:
                return "Normal weight"
            elif 25 <= bmi < 30:
                return "Overweight"
            else:
                return "Obese"
    elif gender == 'female':
        if age < 18:
            if bmi < 16:
                return "Severely underweight"
            elif 16 <= bmi < 17:
                return "Underweight"
            elif 17 <= bmi < 23:
                return "Normal weight"
            elif 23 <= bmi < 25:
                return "Overweight"
            else:
                return "Obese"
        else:
            if bmi < 18.5:
                return "Underweight"
            elif 18.5 <= bmi < 24:
                return "Normal weight"
            elif 24 <= bmi < 29:
                return "Overweight"
            else:
                return "Obese"
    elif gender == 'transgender':
        if age < 18:
            if bmi < 16:
                return "Severely underweight"
            elif 16 <= bmi < 17:
                return "Underweight"
            elif 17 <= bmi < 23:
                return "Normal weight"
            elif 23 <= bmi < 25:
                return "Overweight"
            else:
                return "Obese"
        else:
            if bmi < 18.5:
                return "Underweight"
            elif 18.5 <= bmi < 24:
                return "Normal weight"
            elif 24 <= bmi < 29:
                return "Overweight"
            else:
                return "Obese"
            
            
    else:
        return "Invalid gender"

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    if request.method == 'POST':
        weight_kg = float(request.form['weight'])
        height_m = float(request.form['height'])
        gender = request.form['gender']
        age = int(request.form['age'])

        bmi = calculate_bmi(weight_kg, height_m)
        bmi_category = interpret_bmi(bmi, gender, age)

        return render_template('result.html', bmi=bmi, category=bmi_category)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
