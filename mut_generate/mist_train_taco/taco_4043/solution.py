"""
QUESTION:
Chef loves triangles. But the chef is poor at maths. Given three random lengths Chef wants to find if the three sides form a right-angled triangle or not. Can you help Chef in this endeavour?

-----Input:-----
- First-line will contain $T$, the number of test cases. Then the test cases follow. 
- Each test case contains a single line of input, three Integers $A,B and C$

-----Output:-----
For each test case, output in a single line "YES" if it is possible to form a triangle using the given numbers or "NO" if it is not possible to form a triangle.

-----Constraints-----
- $1 \leq T \leq 1000000$
- $0 \leq A,B,C \leq 100$

-----Sample Input:-----
2
3 4 5
1 3 4

-----Sample Output:-----
YES
NO

-----EXPLANATION:-----
3,4,5 forms a right-angled triangle. 1, 3 and 4 does not form a right-angled triangle.
"""

def is_right_angled_triangle(a, b, c):
    # Check if any side is zero
    if a == 0 or b == 0 or c == 0:
        return 'NO'
    
    # Check all permutations of the sides to see if they form a right-angled triangle
    sides = [a, b, c]
    for _ in range(3):
        if sides[0]**2 == sides[1]**2 + sides[2]**2:
            return 'YES'
        sides.append(sides.pop(0))  # Rotate the sides
    
    return 'NO'