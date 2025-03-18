import pytest
import hashlib
import string
import password_generator.core as core

def test_generate():
    password = core.generate(10)
    assert isinstance(password, str)
    assert len(password) == 10

def test_generate_upper():
    password = core.generate(10, capitalize = True)
    assert isinstance(password, str)
    assert any(char.isupper() for char in password)

def test_generate_number():
    password = core.generate(10, numbers = True)
    assert isinstance(password, str)
    assert any(char.isdigit() for char in password)

def test_generate_symbol():
    password = core.generate(10, symbols = True)
    assert isinstance(password, str)
    assert any(char in string.punctuation for char in password)

def test_generate_number_cap():
    password = core.generate(10, numbers = True, capitalize = True)
    assert isinstance(password, str)
    assert any(char.isdigit() for char in password)
    assert any(char.isupper() for char in password)

def test_generate_number_symbol():
    password = core.generate(10, numbers = True, symbols = True)
    assert isinstance(password, str)
    assert any(char.isdigit() for char in password)
    assert any(char in string.punctuation for char in password)

def test_generate_cap_symbol():
    password = core.generate(10, capitalize = True, symbols = True)
    assert isinstance(password, str)
    assert any(char.isupper() for char in password)
    assert any(char in string.punctuation for char in password)

def test_generate_number_cap_symbol():
    password = core.generate(10, numbers = True, capitalize = True, symbols = True)
    assert isinstance(password, str)
    assert any(char.isdigit() for char in password)
    assert any(char.isupper() for char in password)
    assert any(char in string.punctuation for char in password)

def test_caesar_cipher():
    pass

def test_scramble():
    test_cases = ["hello", "shaurya", "asjdkd7832", "nsdkajkkadj!askd&", "kjaibbd88*jsd8"]
    for test in test_cases:
        scrambled_string = core.scramble(test)
        assert len(test) == len(scrambled_string)
        char_list_test = [char for char in test]
        char_list_scrambled = [char for char in scrambled_string]
        for char in char_list_test:
            assert char in char_list_scrambled

def test_binary_password():
    bin_password = core.binary_password(10)
    assert isinstance(bin_password, str)
    assert len(bin_password) == 10
    bitlist = list('01')
    for char in bin_password:
        assert char in bitlist

def test_generateHash():
    pass_hash = core.generateHash("password")
    assert isinstance(pass_hash, str)
    assert len(pass_hash) == 64
