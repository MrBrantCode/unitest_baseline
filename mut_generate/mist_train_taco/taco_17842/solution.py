"""
QUESTION:
The preferred way to generate user login in Polygon is to concatenate a prefix of the user's first name and a prefix of their last name, in that order. Each prefix must be non-empty, and any of the prefixes can be the full name. Typically there are multiple possible logins for each person.

You are given the first and the last name of a user. Return the alphabetically earliest login they can get (regardless of other potential Polygon users).

As a reminder, a prefix of a string s is its substring which occurs at the beginning of s: "a", "ab", "abc" etc. are prefixes of string "{abcdef}" but "b" and 'bc" are not. A string a is alphabetically earlier than a string b, if a is a prefix of b, or a and b coincide up to some position, and then a has a letter that is alphabetically earlier than the corresponding letter in b: "a" and "ab" are alphabetically earlier than "ac" but "b" and "ba" are alphabetically later than "ac".


-----Input-----

The input consists of a single line containing two space-separated strings: the first and the last names. Each character of each string is a lowercase English letter. The length of each string is between 1 and 10, inclusive. 


-----Output-----

Output a single string — alphabetically earliest possible login formed from these names. The output should be given in lowercase as well.


-----Examples-----
Input
harry potter

Output
hap

Input
tom riddle

Output
tomr
"""

def generate_earliest_login(first_name: str, last_name: str) -> str:
    # Initialize the login string with the first character of the first name
    login = first_name[0]
    
    # Iterate through the remaining characters of the first name
    for char in first_name[1:]:
        # If the current character is alphabetically earlier than the first character of the last name, add it to the login
        if char < last_name[0]:
            login += char
        else:
            # Otherwise, break the loop as we need the earliest possible login
            break
    
    # Add the first character of the last name to complete the login
    login += last_name[0]
    
    return login