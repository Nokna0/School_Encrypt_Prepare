def hash(text):
    hash_value = 0

    for i, char in enumerate(text):
        hash_value += ord(char) * i

    return hash_value


target = input()

print(hash(target))