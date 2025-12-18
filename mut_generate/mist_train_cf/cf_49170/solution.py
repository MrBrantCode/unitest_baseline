"""
QUESTION:
Create a function named `decrypt` that takes an encrypted string as input, where each word has its first two letters switched, and returns the decrypted string. The function should also work correctly for words with less than two letters. The input string will be in a comma-separated format with multiple rows separated by semicolons.
"""

def decrypt(encrypted_string):
    data_points = encrypted_string.split(';')
    decrypted_data_points = []

    def decrypt_word(word):
        if len(word) < 2:
            return word
        else:
            return word[1] + word[0] + word[2:]

    for data_point in data_points:
        words = data_point.split(',')
        decrypted_data_point = ",".join([decrypt_word(word) for word in words])
        decrypted_data_points.append(decrypted_data_point)

    return "\n".join(decrypted_data_points)