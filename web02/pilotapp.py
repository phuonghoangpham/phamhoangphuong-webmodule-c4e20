from flask import Flask, render_template
import mlab
from mongoengine import *
from models.Service import Service 
#tu folder models vao file service.py import class Service

app = Flask(__name__)
mlab.connect()

#design pattern (MVC, MVP)
#1. Design DB
class Service(Document):  #viet hoa chu cai dau tien cua collection
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField ()
    phone = StringField ()
    address = StringField()
    status = BooleanField ()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<g>')
def search(g):
    all_service = Service.objects(gender=g, yob__lte=1998, height__gte=165)
    return render_template('search.html', all_service = all_service)

if __name__ == '__main__':
  app.run(debug=True)
 