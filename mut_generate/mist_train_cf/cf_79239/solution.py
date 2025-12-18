"""
QUESTION:
Write a function `binary_conversion(num1, num2)` that calculates the least number of swaps needed to transform one binary number string `num1` into another distinct binary number string `num2` of the same length. The function should also return a list of pairs, where each pair represents the positions (1-indexed from right to left) of the two binary digits swapped. If multiple swap sequences result in the least number of swaps, any one of them is acceptable.
"""

def binary_conversion(num1, num2):
    n1 = len(num1)
    n2 = len(num2)
    if n1 != n2:
        return 'Binary numbers should be of equal length'
    swaps = []
    swap_count = 0
    i = n2 - 1
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