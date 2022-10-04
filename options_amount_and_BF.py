def options_amount():
    bit_amount = int(input('How many bits in sequence?(8,16,32,64,128,256,512,1024,2048,4096): '))
    return 2 ** bit_amount


print(options_amount())
