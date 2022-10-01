def caesar_cipher(text, step):
    encrypt = ''
    char_map = 'abcdefghijklmnopqrstuvwxyz'
    step %= len(char_map)
    encrypt_map = char_map[step:] + char_map[:step]

    char_map += char_map.upper()
    encrypt_map += encrypt_map.upper()

    for char in text:
        new_char = char
        index = char_map.find(char)
        if index >= 0:
            new_char = encrypt_map[index]
        encrypt += new_char
    return encrypt
