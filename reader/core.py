import random
import math

def __init__(self, length, digit, password=''):
     self.length = length
     self.digit = digit
     self.password = password

def __str__ ():
    pass
#Sets length of the password
def setLength(length):
    pass

def allowDigit(bool):
    pass

def generate():
    pass


 #Sets if the password is funny or not
def allowDigit(t):
    pass

 #Generate password
def generate():
    pass
 #returns all the parameters
def  parameters():
    pass

#scrambles a given string
def scramble(self, string):
    toList = [chr for chr in string]
    print(toList)
    retString = ''
    while len(toList) > 0:
        rand = math.floor(random.random() * len(toList))
        letter = toList.pop(rand)
        retString = retString + letter
    self.password = retString


#does a cesar cipher on a string
def cesar_cipher(string):
    pass

 #returns the current password
def retPassword():
    pass

