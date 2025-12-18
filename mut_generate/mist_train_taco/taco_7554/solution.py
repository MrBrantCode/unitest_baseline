"""
QUESTION:
Sensation, sensation in the two-dimensional kingdom! The police have caught a highly dangerous outlaw, member of the notorious "Pihters" gang. The law department states that the outlaw was driving from the gang's headquarters in his car when he crashed into an ice cream stall. The stall, the car, and the headquarters each occupies exactly one point on the two-dimensional kingdom.

The outlaw's car was equipped with a GPS transmitter. The transmitter showed that the car made exactly n movements on its way from the headquarters to the stall. A movement can move the car from point (x, y) to one of these four points: to point (x - 1, y) which we will mark by letter "L", to point (x + 1, y) — "R", to point (x, y - 1) — "D", to point (x, y + 1) — "U".

The GPS transmitter is very inaccurate and it doesn't preserve the exact sequence of the car's movements. Instead, it keeps records of the car's possible movements. Each record is a string of one of these types: "UL", "UR", "DL", "DR" or "ULDR". Each such string means that the car made a single movement corresponding to one of the characters of the string. For example, string "UL" means that the car moved either "U", or "L".

You've received the journal with the outlaw's possible movements from the headquarters to the stall. The journal records are given in a chronological order. Given that the ice-cream stall is located at point (0, 0), your task is to print the number of different points that can contain the gang headquarters (that is, the number of different possible locations of the car's origin).

Input

The first line contains a single integer n (1 ≤ n ≤ 2·105) — the number of the car's movements from the headquarters to the stall.

Each of the following n lines describes the car's possible movements. It is guaranteed that each possible movement is one of the following strings: "UL", "UR", "DL", "DR" or "ULDR". 

All movements are given in chronological order. 

Please do not use the %lld specifier to read or write 64-bit integers in C++. It is preferred to use the cin and cout stream or the %I64d specifier.

Output

Print a single integer — the number of different possible locations of the gang's headquarters.

Examples

Input

3
UR
UL
ULDR


Output

9


Input

2
DR
DL


Output

4

Note

The figure below shows the nine possible positions of the gang headquarters from the first sample: 

<image>

For example, the following movements can get the car from point (1, 0) to point (0, 0): 

<image>
"""

def count_possible_headquarters(n: int, movements: list) -> int:
    """
    Calculate the number of different possible locations of the gang's headquarters
    based on the given movements.

    Parameters:
    n (int): The number of movements.
    movements (list): A list of strings representing the possible movements.

    Returns:
    int: The number of different possible locations of the gang's headquarters.
    """
    r = 1
    c = 1
    for s in movements:
        if len(s) == 4:
            r += 1
            c += 1
        elif s == 'UL' or s == 'DR':
            r += 1
        else:
            c += 1
    return r * c