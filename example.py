from passgenpy import core as cd

# Generate a simple 8-character password
password = cd.generate(8)
# Sample output:

# Generate a complex 12-character password with all options
complex_password = cd.generate(12, capitalize=True, numbers=True, symbols=True)
# Sample output: wjtaxzvk

# Use 3 shift Caesar cipher on "Hello"
encrypted = cd.caesar_cipher("Hello", 3)
# Sample output: Khoor

# Random scramble of "Hello World"
scrambled = cd.scramble("Hello World")
# Sample output: erodlWlHl o

# Binary password of length 8
binary = cd.binary_password(8)
# Sample output: 00110000

# Generate hash for "myPassword123"
hashed = cd.generateHash("myPassword123")
# Sample output: 71d4ec024886c1c8e4707fb02b46fd568df44e77dd5055cadc3451747f0f2716

# Generate a funny password:
funny_pass = cd.getFunnyPassword()
# Sample output: 1sadblackfish