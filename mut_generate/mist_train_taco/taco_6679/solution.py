"""
QUESTION:
The chef was chatting with his friend who was a mathematician.
Chef said "Hi !".

His friend replied that '!' is the symbol of factorial.

Chef had never heard about it and he asked more about it. Then his friend taught him how to calculate the factorial of a number.

Chef loved that But as always he got tired after calculating a few values and asked you to do it for him.

-----Input-----
N : Number of inputs
then N lines with input T

N<10

T<=200

-----Output-----
The result for the corresponding value of T

-----Example-----
Input:
3
5
4
6

Output:
120
24
720
"""

def calculate_factorials(inputs):
    # Precompute factorials up to 200
    factorials = [1]
    for x in range(1, 201):
        factorials.append(factorials[x - 1] * x)
    
    # Calculate the factorial for each input
    results = [factorials[n] for n in inputs]
    
    return results