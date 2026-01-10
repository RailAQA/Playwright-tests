from faker import Faker


fake = Faker()

def generated_random_text() -> str:
    return fake.first_name()

def generate_random_valid_email() -> str:
    return fake.email()