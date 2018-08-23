from models.Customer import Customer
import mlab

mlab.connect()

# id_to_find = "5b7be22918fca375eafae0d9"

# #amanda = Customer.objects(id=id_to_find) ## => []

# #amanda = Customer.objects.get(id=id_to_find) ## => Service object

# customer = Customer.objects.with_id(id_to_find) ## => Service object

# if customer is not None:
#     #print(amanda.name)
#     #customer.delete()
#     #print("Deleted")
#     print("Before: ")
#     print(customer.to_mongo()) #print(customer.yob)
#     customer.update(set__yob=2005, set__name="Linh cute")
#     customer.reload()
#     print("After: ")
#     print(customer.to_mongo())

# else:
#     print("Not found")

all_customer = Customer.objects()

first_customer = all_customer[0]

print(first_customer['name'])