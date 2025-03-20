import random
import string
import math
import hashlib

def generate(length, capitalize=False, numbers=False, symbols=False):
    if type(length) != int:
        raise ValueError("Length Must be an integer!!")
    if type(capitalize) != bool:
        raise ValueError("Capitalize Must be a boolean!!")
    if type(numbers) != bool:
        raise ValueError("Numbers value must be a boolean!!")
    if type(symbols) != bool:
        raise ValueError("Symbols value must be a boolean!!")
    list_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    list_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    list_numbers = '0123456789'
    list_symbols = '!@#$%^&*()-_+=[]{}|:;,./?~'
    all_chars = list_lowercase
    password = [random.choice(list_lowercase)]
    if capitalize:
        all_chars+=list_uppercase
        password.append(random.choice(list_uppercase))
    if numbers:
        all_chars+=list_numbers
        password.append(random.choice(list_numbers))
    if symbols:
        all_chars+=list_symbols
        password.append(random.choice(list_symbols))
    while len(password) < length:
        password.append(random.choice(all_chars))
    return ''.join(password)


#does a cesar cipher on a string
def caesar_cipher(word, shift):
    if type(word) != str:
        raise ValueError("Input must be a string!")
    if type(shift) != int:
        raise ValueError("Shift value must be an integer!")
    try:
        tempShift = int(shift)
    except ValueError:
        raise ValueError("Shift must be an int")
    if float(shift) % 1 != 0.0:
        raise ValueError("Shift must be an int")
    if not (1 <= tempShift <= 25):
        raise ValueError("Shift value must be between 1 and 25.")
    def shift_letter(char, shift):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            return chr((ord(char) - base + shift) % 26 + base)
        return char

    return ''.join(shift_letter(char, tempShift) for char in word)


def scramble(string):
    if type(string) != str:
        raise ValueError("Input must be a string!")
    toList = [chr for chr in string]
    retString = ''
    while len(toList) > 0:
        rand = math.floor(random.random() * len(toList))
        letter = toList.pop(rand)
        retString = retString + letter
    return retString

def binary_password(l):
    if type(l) != int:
        raise ValueError("Length input must be an integer!")
    retString = ''
    for _ in range(l):
        retString+= str(random.randint(0,1))
    return retString

def generateHash(password):
    if type(password) != str:
        raise ValueError("Password must be a string")
    return hashlib.sha256(password.encode()).hexdigest()

def getFunnyPassword():
    funny_list_1 = list('123456789')
    funny_list_2= ["sleepy", "hungry", "tired", "angry", "happy", "sad", "excited", "confused", "bored", "nervous", "excited", "happy", "sad", "angry", "tired", "sleepy", "hungry", "bored", "confused", "nervous"]
    funny_list_3= ["cats", "dogs", "birds", "fish", "snakes", "cows", "horses", "sheep", "goats", "pigs", "chickens", "ducks", "turkeys", "geese", "peacocks", "parrots", "penguins", "ostriches", "eagles", "owls", "sparrows", "roosters", "hens", "peahens", "roosters"]
    funny_list_4= ["orange", "red", "blue", "green", "yellow", "purple", "pink", "brown", "black", "white", "gray", "gold", "silver", "bronze", "copper", "iron", "steel", "gold", "silver", "bronze", "copper", "iron", "steel"]
    return random.choice(funny_list_1) + random.choice(funny_list_2) + random.choice(funny_list_4) + random.choice(funny_list_3)


