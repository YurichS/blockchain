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
        x = (ord(data[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return "".join(cipher_text), key


def vigenere_cipher_decrypted(data, key):
    text = []
    for i in range(len(data)):
        x = (ord(data[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        text.append(chr(x))
    return "".join(text)


# print(vigenere_cipher("Enter your text here", "Enter your key here")[0])
# for vigenere cipher decryption
# key = vigenere_cipher("GEEKSFORGEEKS", "AYUSH")[1] # You can get key in this way
# print(vigenere_cipher_decrypted("Encrypted text", "Key"))


def rsa(data):
    p = 173  # any large prime number
    q = 149
    n = p * q
    e = 234
    d = (5 * (p - 1) * (q - 1) + 1) / e
    return (data ** e) % n

# print(rsa("Enter your number"))
