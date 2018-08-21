from flask import Flask, render_template
import mlab
from mongoengine import *
from models.Customer import Customer 

app = Flask(__name__)
mlab.connect()

class Customer(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    phone = StringField ()
    address = StringField()
    contacted = BooleanField ()
    email = StringField()
    job = StringField()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customer/<int:g>')
def customer(g):
    all_customer = Customer.objects[:10](gender = g, contacted = False)
    return render_template('showcustomer.html', all_customer = all_customer)

if __name__ == '__main__':
  app.run(debug=True)
 