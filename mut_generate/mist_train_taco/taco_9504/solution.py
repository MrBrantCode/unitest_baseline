"""
QUESTION:
You are provided with an input containing a number. Implement a solution to find the largest sum of consecutive increasing digits , and present the output with the largest sum and the positon of start and end of the consecutive digits.
Example :
Input :> 8789651
Output :> 24:2-4
where 24 is the largest sum and 2-4 is start and end of the consecutive increasing digits.
"""

def find_largest_consecutive_increasing_digits(number_str):
    l = list(map(int, number_str))
    t = -1
    x = -1
    y = -1
    
    for i in range(len(l)):
        s = l[i]
        a = i + 1
        b = i + 1
        for j in range(i + 1, len(l)):
            if l[i] < l[j]:
                s = s + l[j]
                b = j + 1
            else:
                break
        if s > t:
            t = s
            x = a
            y = b
    
    return t, x, y