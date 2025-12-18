"""
QUESTION:
Design a function named `reverse_sequences` that takes a list of strings as input. The function should return a list of strings where each string is the reverse of the corresponding input string with all special characters removed. The function should not use any built-in reverse function and should use a recursive approach to reverse the strings.
"""

def reverse_sequences(sequences):
    def remove_special_chars(text):
        cleaned_text = ""
        for char in text:
            #check if alphanumeric
            if char.isalnum():
                cleaned_text += char
        return cleaned_text

    def reverse_string(text, index):
        if index < 0:
            return ""
        else:
            return text[index] + reverse_string(text, index-1)

    reversed_seq = []
    for sequence in sequences:
        cleaned_seq = remove_special_chars(sequence)
        reversed_string = reverse_string(cleaned_seq, len(cleaned_seq)-1)
        reversed_seq.append(reversed_string)
    return reversed_seq