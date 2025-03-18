import random
import string
import math
import hashlib

def generate(length, capitalize=False, numbers=False, symbols=False):
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
def caesar_cipher(password, shift):
    if not (1 <= shift <= 25):
        raise ValueError("Shift value must be between 1 and 25.")

    def shift_letter(char, shift):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            return chr((ord(char) - base + shift) % 26 + base)
        return char

    return ''.join(shift_letter(char, shift) for char in  password)


def scramble(self, string):
    toList = [chr for chr in string]
    retString = ''
    while len(toList) > 0:
        rand = math.floor(random.random() * len(toList))
        letter = toList.pop(rand)
        retString = retString + letter
    return retString

def binary_password(len):
    retString = ''
    for _ in range(len):
        retString+= str(random.randint(0,1))
    return retString

def generateHash(password):
    return hashlib.sha256(password.encode()).hexdigest()

def getFunnyPassword():
    funny_list_1 = list('123456789')
    funny_list_2= ["sleepy", "hungry", "tired", "angry", "happy", "sad", "excited", "confused", "bored", "nervous", "excited", "happy", "sad", "angry", "tired", "sleepy", "hungry", "bored", "confused", "nervous"]
    funny_list_3= ["cats", "dogs", "birds", "fish", "snakes", "cows", "horses", "sheep", "goats", "pigs", "chickens", "ducks", "turkeys", "geese", "peacocks", "parrots", "penguins", "ostriches", "eagles", "owls", "sparrows", "roosters", "hens", "peahens", "roosters"]
    funny_list_4= ["orange", "red", "blue", "green", "yellow", "purple", "pink", "brown", "black", "white", "gray", "gold", "silver", "bronze", "copper", "iron", "steel", "gold", "silver", "bronze", "copper", "iron", "steel"]
    return random.choice(funny_list_1) + random.choice(funny_list_2) + random.choice(funny_list_4) + random.choice(funny_list_3)


