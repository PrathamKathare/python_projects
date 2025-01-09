import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def password_generator():
    while True:
        x = input("Password length? (Type 'exit' to stop): ")
        if x.lower() == 'exit':
            break
        try:
            x = int(x)
            print(generate_random_string(x))
            if input("Generate another? (yes/no): ").lower() != 'yes':
                break
        except ValueError:
            pass

password_generator()
