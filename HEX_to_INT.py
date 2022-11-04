def hex_to_little_endian(number):
    result = bytearray.fromhex(number)[::-1]
    return int(bytearray.hex(result), base=16)


def hex_to_big_endian(number):
    result = bytearray.fromhex(number)
    return int(bytearray.hex(result), base=16)


def little_endian_to_hex(number, bytes_amount):
    return int(number).to_bytes(bytes_amount, "little").hex()


def big_endian_to_hex(number, bytes_amount):
    return int(number).to_bytes(bytes_amount, "big").hex()


