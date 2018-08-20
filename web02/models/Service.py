from mongoengine import *

class Service(Document):  #viet hoa chu cai dau tien cua collection
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField ()
    phone = StringField ()
    address = StringField()
    status = BooleanField ()