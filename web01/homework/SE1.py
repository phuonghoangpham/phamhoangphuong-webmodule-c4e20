#without using render_template

from flask import Flask
app = Flask(__name__)

@app.route('/BMI1/<int:weight>/<int:height>')
def calc_BMI1(weight,height):
    BMI=str((10000*weight//height)//height)
    if int(float(BMI)) < 16:
        return "Your BMI is {} and you are severely underweight".format(BMI)
    elif 16<=int(float(BMI))<=18:
        return "Your BMI is {} and you are underweight".format(BMI)
    elif 18.5<int(float(BMI))<25:
        return "Your BMI is {} and you are normal".format(BMI)
    elif 25<=int(float(BMI))<=30:
       return "Your BMI is {} and you are overweight".format(BMI)
    elif int(float(BMI))>30:
       return "Your BMI is {} and you are obese".format(BMI)
    

if __name__ == '__main__': 
  app.run(debug=True)

