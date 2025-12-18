"""
QUESTION:
Connell Sequence is the sequence formed with the first odd number, i.e 1 as its first term. The subsequent terms of the sequence are made up of the first two even numbers, i.e 2 and 4, followed by the next three odd numbers, i.e 5, 7 and 9, followed by the next four even numbers, i.e 10, 12, 14 and 16 and so on …. 
Given an integer n, generate the first n terms of the Connell Sequence.
Example 1:
Input: n = 6
Output: 1 2 4 5 7 9
Explaination: First one odd number. Then 
two even numbers. Then three odd numbers.
 
Example 2:
Input: n = 2
Output: 1 2
Explaination: The sequence consists of first 
odd number then one even number.
 
Your Task:
You do not need to read input or print anything. Your task is to complete the function connellSequence() which takes n as input parmeters and returns a list of integers containing the first n numbers of the Connell sequence.
 
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)
 
Constraints:
1 ≤ n ≤ 10^{5}
"""

def generate_connell_sequence(n: int) -> list[int]:
    sequence = []
    flag = 0  # 0 for odd, 1 for even
    start = 1
    count = 1
    temp = 0
    
    while len(sequence) < n:
        if temp >= start:
            flag = not flag
            start += 1
            temp = 0
        
        if flag == 1:
            if count % 2 == 0:
                temp += 1
                sequence.append(count)
        else:
            if count % 2 == 1:
                temp += 1
                sequence.append(count)
        
        count += 1
    
    return sequence