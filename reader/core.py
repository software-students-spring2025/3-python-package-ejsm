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
def scramble(string):
    pass

#does a cesar cipher on a string
def caesar_cipher(self, shift: int):
    if not (1 <= shift <= 25):
        raise ValueError("Shift value must be between 1 and 25.")

    def shift_letter(char, shift):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            return chr((ord(char) - base + shift) % 26 + base)
        return char

    self.password = ''.join(shift_letter(char, shift) for char in self.password)




 #returns the current password
def retPassword():
    pass

