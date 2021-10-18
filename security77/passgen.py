import string
import random


def generate_random_password(size=16) -> str:
    ## characters to generate password from
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

    ## shuffling the characters
    random.shuffle(characters)
    
    ## picking random characters from the list
    password = []
    for i in range(size):
        password.append(random.choice(characters))

    ## shuffling the resultant password
    random.shuffle(password)

    ## converting the list to string
    ## printing the list
    return "".join(password)
