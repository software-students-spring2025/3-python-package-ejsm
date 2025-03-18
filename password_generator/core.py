import random
import string
import math
import hashlib

def generate(length, capitalize=False, numbers=False, symbols=False):
    password = ''
    list_lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    list_uppercase = [chr(ord(char) - 32) for char in list_lowercase]
    list_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    list_symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', ':', ';', ',', '.', '/', '?', '~']
    rand_lower = [random.randint(0, len(list_lowercase) - 1) for _ in range(5)]
    if capitalize:
        rand_upper = [random.randint(0, len(list_uppercase) - 1) for _ in range(2)]
    if numbers:
        rand_number = [random.randint(0, len(list_numbers) - 1) for _ in range(3)]
    if symbols:
        rand_symbol = [random.randint(0, len(list_symbols) - 1) for _ in range(2)]
    for i in range(length):
        password += list_lowercase[rand_lower[i]]
        if capitalize:
            password += list_uppercase[rand_upper[i]]
        if numbers:
            password += list_numbers[rand_number[i]]

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


