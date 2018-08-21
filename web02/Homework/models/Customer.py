from mongoengine import *

class Customer(Document):  #viet hoa chu cai dau tien cua collection
    name = StringField()
    yob = IntField()
    gender = IntField()
    phone = StringField ()
    address = StringField()
    email = StringField()
    job = StringField()
    contacted = BooleanField ()