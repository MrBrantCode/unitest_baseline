"""
QUESTION:
Rearrange the characters of a given string in the order of their frequency, ensuring that no two adjacent characters are the same.

Given a string consisting of lowercase English letters, create a function named `rearrange_string` to rearrange the characters such that the characters with the highest frequency come first, followed by characters with lower frequencies. The function should ensure that no two adjacent characters are the same and can return any valid rearrangement. The input string length ranges from 1 to 10^5.

Function signature: `def rearrange_string(string: str) -> str:`
"""

def rearrange_string(string: str) -> str:
    # Step 1: Create a dictionary to store the frequency of each character
    frequency = {}
    for char in string:
        frequency[char] = frequency.get(char, 0) + 1

    # Step 2: Sort the characters in descending order of their frequency
    sorted_chars = sorted(frequency.keys(), key=lambda x: frequency[x], reverse=True)

    # Step 3: Initialize an empty string to store the rearranged characters
    result = ""

    # Step 4: Append the sorted characters to the result string while ensuring no two adjacent characters are the same
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

    # Step 5: Return the rearranged characters
    return result