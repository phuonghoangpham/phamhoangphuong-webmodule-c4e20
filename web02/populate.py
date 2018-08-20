from models.Service import Service
import mlab
from faker import Faker
from random import randint, choice


mlab.connect()

faker = Faker()

# name = faker.name()
# print(name)
for i in range (50):
    print("Saving service", i+1, ".......")
    new_service = Service(
        name = faker.name(),
        yob = randint(1990,2000),
        gender = randint(0,1),
        height = randint(150,190),
        phone = faker.phone_number(),
        address = faker.address(),
        status = choice([True, False])
    )

    new_service.save()
