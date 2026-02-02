def hash(text):
    hash_value = 0

    for i, char in enumerate(text):
        hash_value += ord(char) * (i + 1)

    return hash_value

def unhash(hash_value):
    result = ""
    remaining = hash_value
    i = 1
    
    while remaining > 0 and i < 256:
        char_code = remaining // i
        if 32 <= char_code <= 126:
            result += chr(char_code)
            remaining -= char_code * i
        i += 1
    
    return result

target = input("Enter text to hash: ")

hashed_value = hash(target)

print(hashed_value)

print(unhash(hashed_value))