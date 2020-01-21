# hello-world
import sys
import requests
import os
import math
import time


# print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting


r = requests.get('https://www.thesun.co.uk/')
print(r.status_code)

# print(greet('World'))
# print(greet('Ian'))
