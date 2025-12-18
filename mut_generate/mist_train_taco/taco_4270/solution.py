"""
QUESTION:
We've learnt about operators and other basics of CPP. Now, it's time to take another leap and learn to use control structures that helps us choose flow of any code.Given two integers a and b. Your task is to print the even number first and odd number next in individual lines.
Note: Must print end of the line at the end.Example 1:Input: a = 2, b = 3Output: 23Example 2:Input: a = 5, b = 2Output:25
Your Task:
You don't need to read or print anything. Your task is to complete the functionevenOdd()which takes a and b as input parameter and complete the task.
Expected Time Complexity:O(1)
Expected Space Complexity:O(1)Constraints:
1 ≤ a, b ≤ 10^{8}
"""

def even_odd_order(a: int, b: int) -> str:
    if a % 2 == 0:
        return f"{a}\n{b}"
    else:
        return f"{b}\n{a}"