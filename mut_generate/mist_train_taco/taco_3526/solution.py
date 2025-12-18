"""
QUESTION:
Polycarpus has n friends in Tarasov city. Polycarpus knows phone numbers of all his friends: they are strings s1, s2, ..., sn. All these strings consist only of digits and have the same length. 

Once Polycarpus needed to figure out Tarasov city phone code. He assumed that the phone code of the city is the longest common prefix of all phone numbers of his friends. In other words, it is the longest string c which is a prefix (the beginning) of each si for all i (1 ≤ i ≤ n). Help Polycarpus determine the length of the city phone code. 

Input

The first line of the input contains an integer n (2 ≤ n ≤ 3·104) — the number of Polycarpus's friends. The following n lines contain strings s1, s2, ..., sn — the phone numbers of Polycarpus's friends. It is guaranteed that all strings consist only of digits and have the same length from 1 to 20, inclusive. It is also guaranteed that all strings are different.

Output

Print the number of digits in the city phone code.

Examples

Input

4
00209
00219
00999
00909


Output

2


Input

2
1
2


Output

0


Input

3
77012345678999999999
77012345678901234567
77012345678998765432


Output

12

Note

A prefix of string t is a string that is obtained by deleting zero or more digits from the end of string t. For example, string "00209" has 6 prefixes: "" (an empty prefix), "0", "00", "002", "0020", "00209".

In the first sample the city phone code is string "00".

In the second sample the city phone code is an empty string.

In the third sample the city phone code is string "770123456789".
"""

def find_city_phone_code_length(phone_numbers):
    if not phone_numbers:
        return 0
    
    # Initialize the length of the common prefix
    common_prefix_length = 0
    
    # Get the length of the first phone number
    first_phone_number = phone_numbers[0]
    first_phone_length = len(first_phone_number)
    
    # Iterate over each character position in the first phone number
    for i in range(first_phone_length):
        current_char = first_phone_number[i]
        
        # Check if this character matches in all phone numbers
        for phone_number in phone_numbers:
            if phone_number[i] != current_char:
                return common_prefix_length
        
        # If the character matches in all phone numbers, increment the common prefix length
        common_prefix_length += 1
    
    return common_prefix_length