# importing necessary libraries
from random import choices, choice
from time import time


def options_amount():
    """This function returns number of possible keys combinations depending on key length"""
    bit_amount = int(input('How many bits in sequence?(8,16,32,64,128,256,512,1024,2048,4096): '))
    return 2 ** bit_amount


# print(options_amount())


def key_generation():
    """This function returns a hex key with chosen length"""
    bit_amount = int(input('How many bits in sequence?(8,16,32,64,128,256,512,1024,2048,4096): '))
    sign_value = [0, 1]
    hex_numbers = list('0123456789ABCDEF')
    return str(choice(sign_value)) + 'x' + ''.join(choices(hex_numbers, k=bit_amount))


# print(key_generation())


def key_brute_force(key):
    """This function returns time needed to brute force a hex key"""
    start = int(time() * 1000)
    bit_amount = len(key[2:])
    k = 0
    base = "{:0" + str(bit_amount) + "X}"
    while k < 16 ** bit_amount:
        if base.format(k) == key[2:]:
            finish = time() * 1000
            break
        k += 1
    return f"Brute force time: {finish - start}"

# print(key_brute_force('Enter your key'))
