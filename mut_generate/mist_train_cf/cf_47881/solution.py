"""
QUESTION:
Implement a function `divide(dividend, divisor)` that performs integer division without using the division, multiplication, or modulus operators '/, *, %'. The function should handle overflow cases and division by zero, and it should work within the constraints of the 32-bit signed integer range (-2147483648 to 2147483647). The function should return the quotient as an integer, taking into account the signs of the input integers. The time complexity of the solution should be approximately O(log(dividend/divisor)).
"""

def divide(dividend, divisor):
  # Handle divisor 0 case
  if divisor == 0:
    return "Cannot divide by zero!"
  
  # Handle overflow cases
  if dividend == -2147483648 and divisor == -1:
    return 2147483647
  
  # Take care of the signs
  sign = -1 if ((dividend < 0) ^  (divisor < 0)) else 1
  
  # Make divisor and divident positives
  dividend, divisor = abs(dividend), abs(divisor)
  
  quotient = 0
  while dividend >= divisor:
    temp, i = divisor, 1
    while dividend >= temp:
      dividend -= temp
      quotient += i
      i <<= 1
      temp <<= 1
      
  return sign*quotient