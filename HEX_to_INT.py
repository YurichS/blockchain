def hex_to_little_endian(number):
    result = bytearray.fromhex(number)[::-1]
    return int(bytearray.hex(result), base=16)

#print(hex_to_little_endian("Enter HEX number as a string here"))

def hex_to_big_endian(number):
    result = bytearray.fromhex(number)
    return int(bytearray.hex(result), base=16)

# print(hex_to_big_endian("Enter HEX number as a string here"))

def little_endian_to_hex(number, bytes_amount):
    return int(number).to_bytes(bytes_amount, "little").hex()

# print(little_endian_to_hex("Enter Little endian as a string here", "Enter bytes amount as INT here"))

def big_endian_to_hex(number, bytes_amount):
    return int(number).to_bytes(bytes_amount, "big").hex()

# print(big_endian_to_hex("Enter Little endian as a string here", "Enter bytes amount as INT here"))

