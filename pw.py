import random
import string
import requests

def rc():
    choices = string.ascii_letters + string.digits + string.punctuation
    return random.choice(choices)

passwordLength = random.randint(int(input("What is the minimum character length? \n" )), 3911111)


def genstrong():
    password = ""
    for i in range(passwordLength):
        password=password+rc()
    print(password)

genstrong()


def fetch_word():
    url="https://random-word-api.herokuapp.com/word?length=6"

    response=requests.get(url)
    word=response.json()[0]
    return word



def generate_weaker_password():
    word1 = fetch_word()
    word2 = fetch_word()
    password = word1 + word2
    return password

print("\n" + generate_weaker_password())