import random
import string

def strong_password_generator(length):
    alphabets = string.ascii_letters + string.punctuation
    return ''.join(list(random.choice(alphabets) for _ in range(length)))

l = int(input('Enter the expected length of your password: '))
print(strong_password_generator(l))
