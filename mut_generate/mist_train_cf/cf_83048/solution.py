"""
QUESTION:
Write a function `playfair_decrypt(message, key_matrix)` that takes a string `message` and a 5x5 matrix `key_matrix` as input, where `key_matrix` represents the Playfair cipher key, and returns the decrypted message. The function should use the Playfair cipher decryption technique to decrypt the message. The input `message` will be a string of characters, and `key_matrix` will be a 5x5 matrix of characters. The function should return the decrypted message as a string.
"""

def find_position(key_matrix, letter):
    x = y = 0
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == letter:
                x = i
                y = j

    return x, y


def playfair_decrypt(message, key_matrix):
    
    i = 0
    decrypted_text = ''

    while i < len(message):
        x1, y1 = find_position(key_matrix, message[i])
        x2, y2 = find_position(key_matrix, message[i+1])
        if x1 == x2:
            decrypted_text += key_matrix[x1][(y1-1)%5]
            decrypted_text += key_matrix[x2][(y2-1)%5]
        elif y1 == y2:
            decrypted_text += key_matrix[(x1-1)%5][y1]
            decrypted_text += key_matrix[(x2-1)%5][y2]
        else:
            decrypted_text += key_matrix[x1][y2]
            decrypted_text += key_matrix[x2][y1]
        i += 2

    return decrypted_text