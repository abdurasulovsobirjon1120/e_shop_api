import random
import string

def generate_code(son=1):
    return random.randint(10**son, 10**(son+1)-1)

def generate_code_token(length):
    code_token = ''.join(random.choice(string.ascii_letters) for i in range(length))

    return code_token