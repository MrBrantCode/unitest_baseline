"""
QUESTION:
Find the sum of the odd numbers within an array, after cubing the initial integers. The function should return `undefined`/`None`/`nil`/`NULL` if any of the values aren't numbers. 

~~~if:java,csharp
Note: There are ONLY integers in the JAVA and C# versions of this Kata.
~~~

~~~if:python
Note: Booleans should not be considered as numbers.
~~~
"""

def sum_of_cubed_odds(arr):
    # Check if all elements in the array are integers
    if not all(isinstance(n, int) for n in arr):
        return None
    
    # Calculate the sum of the cubes of odd integers
    return sum(n ** 3 for n in arr if n % 2 != 0)