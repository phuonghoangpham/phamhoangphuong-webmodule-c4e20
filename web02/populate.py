from models.Service import Service
import mlab
from faker import Faker
from random import randint


mlab.connect()

faker = Faker()

# name = faker.name()
# print(name)
for i in range (25):
    print("Saving service", i+1, ".......")
    gender = randint(0,1)
    
    if gender == 1:
        new_service = Service(
            name = faker.name(),
            yob = randint(1990,2000),
            gender = randint(0,1),
            height = randint(150,190),
            phone = faker.phone_number(),
            address = faker.address(),
            status = choice([True, False]),
            description = ["ngoan, hiền, dễ bảo, yêu gia đình"],
            measurement = [randint(70,90), randint(60,70), randint(70,90)],
            image = '../static/image/male.jpg'
    )
    else:
        new_service = Service(
            name = faker.name(),
            yob = randint(1990,2000),
            gender = randint(0,1),
            height = randint(150,190),
            phone = faker.phone_number(),
            address = faker.address(),
            status = choice([True, False]),
            description = ["ngoan, hiền, dễ bảo, yêu gia đình"],
            measurement = [randint(70,90), randint(60,70), randint(70,90)],
            image = '../static/image/female.jpg')
    new_service.save()