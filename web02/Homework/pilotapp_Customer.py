from flask import *
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

@app.route('/admin')
def admin():
    all_customer = Customer.objects()
    return render_template('admin.html', all_customer = all_customer)

@app.route('/delete/<customer_id>')
def delete(customer_id):
    customer_to_delete = Customer.objects.with_id(customer_id)
    if customer_to_delete is not None:
        customer_to_delete.delete()
        return redirect(url_for('admin'))
    else:
        return "Service not found"
    #return "Deleted " + customer_id

@app.route('/new-customer', methods = ["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template('new-customer.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']

        new_customer = Customer(
            name = name,
            yob = yob,
            phone = phone
        )
#update: set before input value, radio button 
        new_customer.save()
        return redirect(url_for('admin'))
        #return name + yob + phone

if __name__ == '__main__':
  app.run(debug=True)
 