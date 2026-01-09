from faker import Faker


fake = Faker('ru_Ru')

def generated_random_text():
    return fake.text()