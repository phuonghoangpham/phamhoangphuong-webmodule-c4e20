from models.Customer import Customer
import mlab
from faker import Faker
from random import randint, choice

mlab.connect()

faker = Faker()

# name = faker.name()
# print(name)
for i in range (100):
    print("Saving customer", i+1, ".......")
    new_customer = Customer(
        name = faker.name(),
        yob = randint(1940,2000),
        gender = randint(0,1),
        phone = faker.phone_number(),
        address = faker.address(),
        email = faker.email(),
        job = faker.job(),
        contacted = choice([True, False])
    )

    new_customer.save()