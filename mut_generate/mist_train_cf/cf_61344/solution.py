"""
QUESTION:
Maximum 69 Number with a Twist: Given a positive integer `num` consisting only of digits 6 and 9, return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6), along with the index of the digit that was changed. If no change is needed, return -1 as the index. 

Constraints: 1 ≤ num ≤ 10^4 and num's digits are 6 or 9.
"""

def maximum69Number (num):
    num = list(str(num)) 
    index = -1          
    for i in range(len(num)):
        if num[i] == '6':    
            num[i] = '9'     
            index = i        
            break            
    return (int(''.join(num)), index)