#using render_template

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/BMI2/<int:weight>/<int:height>')
def calc_BMI2(weight, height):
    BMI=((10000*weight//height)//height)
    return render_template('BMI2.html', BMI = BMI)

if __name__ == '__main__': 
  app.run(debug=True)