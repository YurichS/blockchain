from random import choices, choice


def options_amount():
    bit_amount = int(input('How many bits in sequence?(8,16,32,64,128,256,512,1024,2048,4096): '))
    return 2 ** bit_amount


#print(options_amount())


def key_generation():
    bit_amount = int(input('How many bits in sequence?(8,16,32,64,128,256,512,1024,2048,4096): '))
    sign_value = [0, 1]
    hex_numbers = list('0123456789ABCDEF')
    return str(choice(sign_value))+'x'+''.join(choices(hex_numbers, k=bit_amount))


print(key_generation())
