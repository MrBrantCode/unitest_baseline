"""
QUESTION:
Create a function named `lucas_numbers` that generates the first `n` numbers in the Lucas number sequence, a series that starts with 2 and 1 and where each subsequent number is the sum of the previous two. Write the function to accommodate any positive integer `n`, but initially test it with `n = 15`.
"""

def lucas_sequence(n):
    lucas = [2, 1]
    
    for i in range(2, n):
        lucas.append(lucas[i-1] + lucas[i-2])
    
    return lucas