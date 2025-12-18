"""
QUESTION:
Implement the function binary_conversion(num1, num2) to convert binary strings num1 and num2 into each other by swapping '1' and '0' at corresponding positions in both strings. The function should return the minimum number of swaps required and a list of tuples representing the positions of the swaps (1-indexed). If the binary strings are not of equal length, return 'Binary numbers should be of equal length'.
"""

def binary_conversion(num1, num2):  
    n1 = len(num1)  
    n2 = len(num2)  
    if n1 != n2:  
        return 'Binary numbers should be of equal length'  
    swaps = []  
    swap_count = 0  
    i = len(num2) - 1  
    while i >= 0:  
        if num1[i] == '1' and num2[i] == '0':  
            j = i - 1  
            while j >= 0:  
                if num1[j] == '0' and num2[j] == '1':  
                    num1 = num1[:j] + '1' + num1[j+1:i] + '0' + num1[i+1:]  
                    num2 = num2[:j] + '0' + num2[j+1:i] + '1' + num2[i+1:]  
                    swaps.append((j+1, i+1))  
                    swap_count += 1  
                    break  
                j -= 1  
        i -= 1  
    return swap_count, swaps  