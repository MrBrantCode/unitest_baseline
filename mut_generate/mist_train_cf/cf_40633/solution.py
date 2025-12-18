"""
QUESTION:
Count the number of valid passwords based on the given policies. Each policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. The function should take a list of strings, where each string contains a password policy and the password it applies to, separated by a colon and a space. The policy format is "min-max letter".

Function name: `count_valid_passwords`

Input: A list of strings representing password policies and passwords.

Output: The number of valid passwords.

Restriction: The input list is well-formed and each string can be split into policy and password as described above.
"""

from typing import List

def count_valid_passwords(passwords: List[str]) -> int:
    valid_count = 0
    for entry in passwords:
        policy, password = entry.split(": ")
        limits, letter = policy.split(" ")
        min_limit, max_limit = map(int, limits.split("-"))
        letter_count = password.count(letter)
        if min_limit <= letter_count <= max_limit:
            valid_count += 1
    return valid_count