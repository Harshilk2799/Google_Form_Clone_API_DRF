import string
import random

def generateRandomCode():
    res = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return res