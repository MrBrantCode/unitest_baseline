"""
QUESTION:
Given a number K and string str of digits denoting a positive integer, build the largest number possible by performing swap operations on the digits of str at most K times.
Example 1:
Input:
K = 4
str = "1234567"
Output:
7654321
Explanation:
Three swaps can make the
input 1234567 to 7654321, swapping 1
with 7, 2 with 6 and finally 3 with 5
Example 2:
Input:
K = 3
str = "3435335"
Output:
5543333
Explanation:
Three swaps can make the input
3435335 to 5543333, swapping 3 
with 5, 4 with 5 and finally 3 with 4 
Your task:
You don't have to read input or print anything. Your task is to complete the function findMaximumNum() which takes the string and an integer as input and returns a string containing the largest number formed by perfoming the swap operation at most k times.
Expected Time Complexity: O(n!/(n-k)!) , where n = length of input string
Expected Auxiliary Space: O(n)
Constraints:
1 ≤ |str| ≤ 30
1 ≤ K ≤ 10
"""

def find_maximum_number(s: str, k: int) -> str:
    def solve(string, k, index, maxi):
        if k <= 0 or index >= len(string) - 1:
            return
        max_ = string[index]
        for i in range(index + 1, len(string)):
            if int(max_) < int(string[i]):
                max_ = string[i]
        if string[index] != max_:
            k -= 1
        for i in range(index, len(string)):
            if max_ == string[i]:
                (string[index], string[i]) = (string[i], string[index])
                new_str = ''.join(string)
                if int(new_str) > int(maxi[0]):
                    maxi[0] = new_str
                solve(string, k, index + 1, maxi)
                (string[index], string[i]) = (string[i], string[index])

    maxi = [s]
    string = [char for char in s]
    index = 0
    solve(string, k, index, maxi)
    return maxi[0]