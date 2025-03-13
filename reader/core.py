import random
import string

def __init__(self, length, digit, password=''):
     self.length = length
     self.digit = digit
     self.password = password

def __str__ (self):
    return self.password or "No password set"
#Sets length of the password
def setLength(self, length):
    self.length = length

def allowDigit(self,bool):
    self.digit = bool

def generate(self):
    if self.digit:
        self.password = ''.join(random.choices(string.ascii_letters + string.digits, k=self.length))
    else:
        self.password = ''.join(random.choices(string.ascii_letters, k=self.length))

 #returns all the parameters
def parameters(self):
    return f"Length: {self.length}, Digit: {self.digit}, Password: {self.password}"

#scrambles a given string
def scramble(self, string):
    pass

#does a cesar cipher on a string
def cesar_cipher(string):
    pass

 #returns the current password
def retPassword():
    pass

def getFunny():
    funny_list_1 = list('123456789')
    funny_list_2= ["sleepy", "hungry", "tired", "angry", "happy", "sad", "excited", "confused", "bored", "nervous", "excited", "happy", "sad", "angry", "tired", "sleepy", "hungry", "bored", "confused", "nervous"]
    funny_list_3= ["cats", "dogs", "birds", "fish", "snakes", "cows", "horses", "sheep", "goats", "pigs", "chickens", "ducks", "turkeys", "geese", "peacocks", "parrots", "penguins", "ostriches", "eagles", "owls", "sparrows", "roosters", "hens", "peahens", "roosters"]
    funny_list_4= ["orange", "red", "blue", "green", "yellow", "purple", "pink", "brown", "black", "white", "gray", "gold", "silver", "bronze", "copper", "iron", "steel", "gold", "silver", "bronze", "copper", "iron", "steel"]
    return random.choice(funny_list_1) + random.choice(funny_list_2) + random.choice(funny_list_4) + random.choice(funny_list_3)


