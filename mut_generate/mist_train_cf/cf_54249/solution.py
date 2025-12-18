"""
QUESTION:
You need to implement a function named `threeEqualParts(arr)` that takes an array of 0s and 1s as input and returns a list `[i, j, decimal_value]` or `[-1, -1, -1]`. The returned list should contain the indices `i` and `j` such that the array can be divided into three non-empty parts, each representing the same binary value. The `decimal_value` should be the decimal equivalent of the binary value represented by each part. If no such division is possible, the function should return `[-1, -1, -1]`. The array has a length between 3 and 3 * 10^4 and contains only 0s and 1s.
"""

def threeEqualParts(arr):
    def calculate_binary_value(arr, start, end):
        result = 0
        for i in range(start, end):
            result = (result << 1) + arr[i]
        return result
    
    ones = sum(arr)
    
    if ones % 3 != 0: 
        return [-1, -1, -1]
    
    if ones == 0: 
        return [0, len(arr) - 1]

    target_ones = ones // 3  
    count = 0  
    part1_end, part2_end, part3_end = None, None, None  

    for i, bit in enumerate(arr):
        if bit == 1:
            count += 1
            if count == target_ones:
                part1_end = i
            elif count == 2 * target_ones:
                part2_end = i
            elif count == 3 * target_ones:
                part3_end = i

    part1_val = calculate_binary_value(arr, 0, part1_end + 1)  
    part2_val = calculate_binary_value(arr, part1_end + 1, part2_end + 1) 
    part3_val = calculate_binary_value(arr, part2_end + 1, part3_end + 1)  
    if part1_val == part2_val == part3_val:
        return [part1_end - (len(arr) - 1 - part3_end), part2_end - (len(arr) - 1 - part3_end) + 1, part3_val]  
    else:
        return [-1, -1, -1]