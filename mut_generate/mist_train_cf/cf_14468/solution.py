"""
QUESTION:
Write a function called `multiply_large_numbers` that takes two strings of digits `num1` and `num2` as input, each representing a non-negative integer with at most 100 digits, and returns their product as a string. The function should have a time complexity of O(n), where n is the number of digits in the larger integer.
"""

def multiply_large_numbers(num1, num2):
    len1 = len(num1)
    len2 = len(num2)
    
    # Create a result array to store the product of each digit
    result = [0] * (len1 + len2)
    
    # Traverse the first number from right to left
    for i in range(len1 - 1, -1, -1):
        carry = 0
        
        # Traverse the second number from right to left
        for j in range(len2 - 1, -1, -1):
            # Multiply the current digits and add the carry
            temp = int(num1[i]) * int(num2[j]) + result[i + j + 1] + carry
            
            # Add the product to the corresponding position in the result array
            result[i + j + 1] = temp % 10
            
            # Calculate the carry
            carry = temp // 10
        
        # If there's still a carry, add it to the previous position in the result array
        result[i] += carry
    
    # Remove leading zeros from the result array
    start = 0
    while start < len(result) - 1 and result[start] == 0:
        start += 1
    
    # Convert the result array to a string and return it
    return ''.join(map(str, result[start:]))