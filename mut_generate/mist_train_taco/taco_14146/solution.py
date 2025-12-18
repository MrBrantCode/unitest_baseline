"""
QUESTION:
While swimming at the beach, Mike has accidentally dropped his cellphone into the water. There was no worry as he bought a cheap replacement phone with an old-fashioned keyboard. The keyboard has only ten digital equal-sized keys, located in the following way: [Image] 

Together with his old phone, he lost all his contacts and now he can only remember the way his fingers moved when he put some number in. One can formally consider finger movements as a sequence of vectors connecting centers of keys pressed consecutively to put in a number. For example, the finger movements for number "586" are the same as finger movements for number "253": [Image]  [Image] 

Mike has already put in a number by his "finger memory" and started calling it, so he is now worrying, can he be sure that he is calling the correct number? In other words, is there any other number, that has the same finger movements?


-----Input-----

The first line of the input contains the only integer n (1 ≤ n ≤ 9) — the number of digits in the phone number that Mike put in.

The second line contains the string consisting of n digits (characters from '0' to '9') representing the number that Mike put in.


-----Output-----

If there is no other phone number with the same finger movements and Mike can be sure he is calling the correct number, print "YES" (without quotes) in the only line.

Otherwise print "NO" (without quotes) in the first line.


-----Examples-----
Input
3
586

Output
NO

Input
2
09

Output
NO

Input
9
123456789

Output
YES

Input
3
911

Output
YES



-----Note-----

You can find the picture clarifying the first sample case in the statement above.
"""

def can_be_unique_number(n: int, s: str) -> str:
    """
    Determines if the given phone number has unique finger movements on a specific keyboard layout.

    Parameters:
    n (int): The number of digits in the phone number.
    s (str): The phone number string consisting of digits from '0' to '9'.

    Returns:
    str: "YES" if the phone number has unique finger movements, otherwise "NO".
    """
    sp1 = ['1', '4', '7']
    sp2 = ['1', '2', '3']
    sp3 = ['3', '6', '9']
    sp4 = ['7', '0', '9']
    
    if any(i in s for i in sp2):
        if '0' in s:
            return 'YES'
        else:
            if any(j in s for j in sp1) and any(k in s for k in sp3) and any(t in s for t in sp4):
                return 'YES'
    
    return 'NO'