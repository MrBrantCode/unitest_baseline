"""
QUESTION:
Rearrange the characters of a given string of lowercase English letters in the order of their frequency, ensuring that no two adjacent characters are the same. The function should take a string as input and return the rearranged string. 

Function signature: `def rearrange_string(string: str) -> str:`

Input: A string `string` consisting of lowercase English letters. (1 ≤ len(string) ≤ 10^5)

Output: A string representing the rearranged characters of the given string.
"""

def rearrange_string(string: str) -> str:
    # Create a dictionary to store the frequency of each character
    frequency = {}
    for char in string:
        frequency[char] = frequency.get(char, 0) + 1

    # Sort the characters in descending order of their frequency
    sorted_chars = sorted(frequency.keys(), key=lambda x: frequency[x], reverse=True)

    # Initialize an empty string to store the rearranged characters
    result = ""

    # Append the sorted characters to the result string while ensuring no two adjacent characters are the same
    prev_char = None
    for char in sorted_chars:
        if prev_char != char:
            result += char
            frequency[char] -= 1
            if frequency[char] == 0:
                del frequency[char]
            prev_char = char
        else:
            # If there are no more characters available, break the loop
            if not frequency:
                break

            # Find the next character that is not equal to the current character
            for next_char in frequency.keys():
                if next_char != char:
                    break

            # Append the next character to the result string
            result += next_char
            frequency[next_char] -= 1
            if frequency[next_char] == 0:
                del frequency[next_char]

            # Swap the next character with the current character to ensure no two adjacent characters are the same
            frequency[char] = frequency.get(char, 0) + 1
            sorted_chars.append(char)

    # Return the rearranged characters
    return result