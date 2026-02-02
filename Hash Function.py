def hash(text):
    hash_value = 0

    for i, char in enumerate(text):
        hash_value += ord(char) * i

    return hash_value

def unhash(hash_value):
    result = ""
    remaining = hash_value
    i = 1
    
    while remaining > 0 and i < 256:
        if i != 0:
            char_code = remaining // i
            if 32 <= char_code <= 126:
                result += chr(char_code)
                remaining -= char_code * i
        i += 1
    
    return result

print(hash(input()))

print(unhash(hash(input())))