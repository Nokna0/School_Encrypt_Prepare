def encrypt(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result

def decrypt(text, shift=3):
    return encrypt(text, -shift)

message = input("문자열 입력: ")
encrypted = encrypt(message, 3)
decrypted = decrypt(encrypted, 3)

print(f"원본: {message}")
print(f"암호화된 문자열: {encrypted}")
print(f"복호화된 문자열: {decrypted}")