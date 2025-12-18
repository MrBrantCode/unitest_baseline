"""
QUESTION:
Write a function `countAndSay` that takes an integer `n` as input and returns the nth number in a sequence where each number is formed by reading the previous number digit by digit, counting the number of consecutive occurrences of each digit, and concatenating the count followed by the digit itself. The function should handle inputs in the range 1 ≤ n ≤ 30.
"""

def countAndSay(n):
    if n == 1:
        return "1"
    
    prev = "1"
    for _ in range(2, n+1):
        curr = ""
        count = 1
        for i in range(1, len(prev)):
            if prev[i] == prev[i-1]:
                count += 1
            else:
                curr += str(count) + prev[i-1]
                count = 1
        curr += str(count) + prev[-1]
        prev = curr
        
    return prev