"""
QUESTION:
Implement a Calculator class with four methods: `add`, `subtract`, `multiply`, and `divide`, each taking two numbers as parameters. The methods should return the sum, difference, product, and quotient of the two numbers respectively. The `divide` method should return "Error: Cannot divide by zero" if the second number is zero. All methods should have a time complexity of O(1).
"""

def add(self, num1, num2):
    return num1 + num2

def subtract(self, num1, num2):
    return num1 - num2

def multiply(self, num1, num2):
    return num1 * num2

def divide(self, num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero"
    return num1 / num2