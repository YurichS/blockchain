def hex_to_little_endian(number):
    result = bytearray.fromhex(number)[::-1]
    return int(bytearray.hex(result), base=16)

def hex_to_big_endian(number):
    result = bytearray.fromhex(number)
    return int(bytearray.hex(result), base=16)


def little_endian_to_hex(number):
    pass


def big_endian_to_hex(number):
    pass


print(hex_to_big_endian('ff00000000000000000000000000000000000000000000000000000000000000'))