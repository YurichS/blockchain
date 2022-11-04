def vigenere_cipher(data, key):
    def generate_key(data, key):
        key = list(key)
        if len(data) == len(key):
            return (key)
        else:
            for i in range(len(data) -
                           len(key)):
                key.append(key[i % len(key)])
        return "".join(key)

    key = generate_key(data, key)
    cipher_text = []
    for i in range(len(data)):
        x = (ord(data[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return "".join(cipher_text)


# print(vigenere_cipher("Enter your text here", "Enter your key here"))


def rsa(data):
    p = 173  # any large prime number
    q = 149
    n = p * q
    e = 234
    d = (5 * (p - 1) * (q - 1) + 1) / e
    return (data ** e) % n


#print(rsa("Enter your number"))
