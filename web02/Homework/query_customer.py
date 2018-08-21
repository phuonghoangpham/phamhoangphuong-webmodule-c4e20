from models.Customer import Customer
import mlab

mlab.connect()

all_customer = Customer.objects()

first_customer = all_customer[0]

print(first_customer['name'])