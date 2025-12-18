"""
QUESTION:
Innokentiy decides to change the password in the social net "Contact!", but he is too lazy to invent a new password by himself. That is why he needs your help. 

Innokentiy decides that new password should satisfy the following conditions:  the length of the password must be equal to n,  the password should consist only of lowercase Latin letters,  the number of distinct symbols in the password must be equal to k,  any two consecutive symbols in the password must be distinct. 

Your task is to help Innokentiy and to invent a new password which will satisfy all given conditions. 


-----Input-----

The first line contains two positive integers n and k (2 ≤ n ≤ 100, 2 ≤ k ≤ min(n, 26)) — the length of the password and the number of distinct symbols in it. 

Pay attention that a desired new password always exists.


-----Output-----

Print any password which satisfies all conditions given by Innokentiy.


-----Examples-----
Input
4 3

Output
java

Input
6 6

Output
python

Input
5 2

Output
phphp



-----Note-----

In the first test there is one of the appropriate new passwords — java, because its length is equal to 4 and 3 distinct lowercase letters a, j and v are used in it.

In the second test there is one of the appropriate new passwords — python, because its length is equal to 6 and it consists of 6 distinct lowercase letters.

In the third test there is one of the appropriate new passwords — phphp, because its length is equal to 5 and 2 distinct lowercase letters p and h are used in it.

Pay attention the condition that no two identical symbols are consecutive is correct for all appropriate passwords in tests.
"""

def generate_password(n: int, k: int) -> str:
    """
    Generates a password of length `n` with exactly `k` distinct lowercase Latin letters,
    ensuring no two consecutive symbols are the same.

    Parameters:
    - n (int): The length of the password.
    - k (int): The number of distinct symbols in the password.

    Returns:
    - str: A password that satisfies the given conditions.
    """
    letters = list(map(chr, range(97, 97 + k)))  # Generate k distinct lowercase letters
    password = []
    current_index = 0
    
    for _ in range(n):
        password.append(letters[current_index])
        current_index = (current_index + 1) % k  # Cycle through the k distinct letters
    
    return ''.join(password)