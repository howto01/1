def encrypt(text,s):
    result = ""
    for char in text:
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result
def decrypt(text,s):
    result = ""
    for char in text:
        if (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result
text = "abcdefghijklmno"
s = 1
cipher = encrypt(text,s)
print("encryption: ", cipher)
print("decryption: ", decrypt(cipher, s))