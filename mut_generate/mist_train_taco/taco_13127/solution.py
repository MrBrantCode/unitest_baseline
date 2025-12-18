"""
QUESTION:
Given four numbers convert:
	a, a decimal number to the binary equivalent
	b, a binary to decimal equivalent
	c, decimal to hexadecimal equivalent
	d, hexadecimal to decimal equivalent
Example 1:
Input :
a = 6
b = 110
c = 20
d = 2A
Output:
110, 6, 14, 42
Explanation:
(6)_{10} = (110)2
(110)_{2} = (6)_{10}
(20)_{10} = (14)_{16}
(2A)_{16} = (42)_{10}
Example 2:
Input:
a = 10 
b = 111 
c = 25 
d = FA
Output:
1010, 7, 19, 250
Explanation:
(10)_{10} = (1010)_{2}
(111)_{2} = (7)_{10}
(25)_{10} = (19)_{16}
(FA)_{16} = (250)_{10}
Your Task:
You don't need to read input or print anything. Your task is to complete the function convert() which takes three integers a, b, c, and string d as input parameters and returns the converted numbers as an array of four strings.
 
Expected Time Complexity: O(log(max(a,b,c)) + |d|)
Expected Auxiliary Space: O(1)
Constraints:
1 <= a,c <= 500
1 <= b <= 100000(base 2)
1 <= d <= 100000(base 16)
"""

def convert_numbers(a: int, b: int, c: int, d: str) -> list[str]:
    # Convert decimal a to binary
    e = bin(a)[2:]
    
    # Convert binary b to decimal
    f = 0
    p = 1
    while b != 0:
        f += p * (b % 10)
        p *= 2
        b //= 10
    
    # Convert decimal c to hexadecimal
    g = hex(c)[2:].upper()
    
    # Convert hexadecimal d to decimal
    p = 1
    m = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    d = d[::-1]
    h = 0
    for i in d:
        if i.isdigit():
            h += int(i) * p
        else:
            h += p * m[i]
        p *= 16
    
    return [e, str(f), g, str(h)]