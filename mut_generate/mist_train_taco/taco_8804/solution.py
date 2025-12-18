"""
QUESTION:
Ranjit wants to design a algorithm such that, if he enters two numbers, all the numbers between these two numbers are listed(except the number divisible by 5 & 3).

BUT the number divisible by both 3 & 5 is also listed (example 30)
The Numbers should be separated by a "," sign

Example- if the two numbers added are- 25 & 44. 

Then the output should be- 26,28,29,30,31,32,34,37,38,41,43

SAMPLE INPUT
25 44

SAMPLE OUTPUT
26,28,29,30,31,32,34,37,38,41,43
"""

def generate_filtered_range(start: int, end: int) -> str:
    alls = []
    for x in range(start + 1, end):
        if x % 15 == 0:
            alls.append(x)
        elif x % 5 == 0:
            continue
        elif x % 3 == 0:
            continue
        else:
            alls.append(x)
    return ",".join(map(str, alls))