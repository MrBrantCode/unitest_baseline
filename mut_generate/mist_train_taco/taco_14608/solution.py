"""
QUESTION:
Bob is preparing to pass IQ test. The most frequent task in this test is `to find out which one of the given numbers differs from the others`. Bob observed that one number usually differs from the others in **evenness**. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

`!` Keep in mind that your task is to help Bob solve a `real IQ test`, which means indexes of the elements start from `1 (not 0)`

##Examples :

 
```python
iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd
```
"""

def find_different_evenness(numbers):
    # Convert the string of numbers into a list of integers
    num_list = list(map(int, numbers.split()))
    
    # Determine the evenness of each number
    evenness = [num % 2 for num in num_list]
    
    # Find the index of the number that differs in evenness
    if evenness.count(0) == 1:
        # If there's only one even number, return its index
        return evenness.index(0) + 1
    else:
        # Otherwise, return the index of the odd number
        return evenness.index(1) + 1