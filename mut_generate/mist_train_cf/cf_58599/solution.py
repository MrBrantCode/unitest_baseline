"""
QUESTION:
Write a function called `factorial(n)` to calculate the factorial of a given number `n` using string manipulation. The function should be able to handle large numbers that exceed the range of standard numerical data types. The input `n` is an integer and the output should be a string representing the factorial of `n`.
"""

def factorial(n): 
    def multiply(num1, num2):
        size_num1 = len(num1)
        size_num2 = len(num2)
        res = [0] * (size_num1 + size_num2)
        
        for i in range(size_num1-1, -1, -1):  
            carry = 0
            n1 = ord(num1[i]) - 48
            for j in range(size_num2-1, -1, -1):
                n2 = ord(num2[j]) - 48
                summ = n1 * n2 + res[i + j + 1] + carry 
                carry = summ // 10
                res[i + j + 1] = summ % 10
            res[i] += carry
  
        result = "".join(map(str, res))

        # remove leading zeros
        new_result = result.lstrip('0')

        if new_result == "":
            return "0"
        return new_result

    num = "1"
    for i in range(1, n + 1): 
        num = multiply(num, str(i)) 
    return num 