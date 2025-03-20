# Password Generator

Our python package provides various password generation and manipulation functions, including a fun password generator that creates hilarious word combinations.

## Installation


```bash
pip install funny-password-generator
```

## Features

The package provides several functions for password generation and manipulation:

### 1. `generate(length, capitalize=False, numbers=False, symbols=False)`
Generates a random password with specified characteristics.

Parameters:
- `length` (int): The desired length of the password
- `capitalize` (bool, optional): Whether to include uppercase letters (default: False)
- `numbers` (bool, optional): Whether to include numbers (default: False)
- `symbols` (bool, optional): Whether to include special symbols (default: False)

Example:
```python
from password_generator import generate

# Generate a simple 8-character password
password = generate(8)

# Generate a complex 12-character password with all options
complex_password = generate(12, capitalize=True, numbers=True, symbols=True)
```

### 2. `caesar_cipher(word, shift)`
Applies a Caesar cipher to the input string.

Parameters:
- `word` (str): The text to encrypt
- `shift` (int): The shift value (must be between 1 and 25)

Example:
```python
from password_generator import caesar_cipher

encrypted = caesar_cipher("Hello", 3)
```

### 3. `scramble(string)`
Randomly scrambles the characters in the input string.

Parameters:
- `string` (str): The text to scramble

Example:
```python
from password_generator import scramble

scrambled = scramble("Hello World")
```

### 4. `binary_password(length)`
Generates a random binary password of specified length.

Parameters:
- `length` (int): The desired length of the binary password

Example:
```python
from password_generator import binary_password

binary = binary_password(8)
```

### 5. `generateHash(password)`
Generates a SHA-256 hash of the input password.

Parameters:
- `password` (str): The password to hash

Example:
```python
from password_generator import generateHash

hashed = generateHash("myPassword123")
```

### 6. `getFunnyPassword()`
Generates a funny password by combining random words from predefined lists.

Example:
```python
from password_generator import getFunnyPassword

funny_pass = getFunnyPassword()
```


