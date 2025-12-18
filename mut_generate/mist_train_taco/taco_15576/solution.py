"""
QUESTION:
Akku likes binary numbers and she likes playing with these numbers. Her teacher once gave her a question.For given value of  L and R, Akku have to find the count of number X, which have only three-set bits in it's binary representation such that "L ≤ X ≤ R".Akku is genius, she solved the problem easily. Can you do it ??
Example 1:
Input:
L = 11 and R = 19 
Output: 4
Explanation:
There are 4 such numbers with 3 set bits in 
range 11 to 19.
11 -> 1011
13 -> 1101
14 -> 1110
19 -> 10011
 
Example 2:
Input:
L = 25 and R = 29
Output: 3
Explanation:
There are 3 such numbers with 3 set bits in
range 25 to 29. 
25 -> 11001 
26 -> 11010 
28 -> 11100
Your Task:  
You don't need to read input or print anything. Your task is to complete the function solve() which takes the integer L and R as input parameters and returns the count of number X, which have only three-set bits in its binary representation such that "L ≤ X ≤ R".
Expected Time Complexity: O(63^{3}) + O(log(R-L))
Expected Auxiliary Space: O(63^{3})
Constraints:
1 ≤ L ≤ R ≤ 10^{18}
"""

def count_numbers_with_three_set_bits(L, R):
    ans = 0
    for i in range(63):
        for j in range(i + 1, 63):
            for k in range(j + 1, 63):
                curr = 0
                curr |= 1 << i
                curr |= 1 << j
                curr |= 1 << k
                if L <= curr <= R:
                    ans += 1
    return ans