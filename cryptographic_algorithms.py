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
# key = vigenere_cipher("Enter your text here", "Enter your key here")[1] # You can get key in this way
# print(vigenere_cipher_decrypted("Encrypted text", "Key"))


def rsa(data):
    def generate_key():
        p = int(input("Enter big prime number: "))
        q = int(input("Enter another big prime number: "))
        n = p * q
        e = (p - 1) * (q - 1) - 1
        d = (5 * e + 1) / e
        return (e, n), (d, n)

    public, private = generate_key()
    data = str.encode(data)
    data = bytes([(i ** public[0]) % public[1] for i in data])
    return data.decode(), public, private


def rsa_decrypt(data, key):
    data = str.encode(data)
    data = bytes([(i ** key[0]) % key[1] for i in data])
    return data.decode()


# print(rsa("12"))
data,public, key = rsa("iloveyou")

print(rsa_decrypt(data, key))
