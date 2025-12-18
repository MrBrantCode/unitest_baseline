"""
QUESTION:
Given an array, return the difference between the count of even numbers and the count of odd numbers. `0` will be considered an even number. 

```
For example:
solve([0,1,2,3]) = 0 because there are two even numbers and two odd numbers. Even - Odd = 2 - 2 = 0.  
```

Let's now add two letters to the last example: 
```
solve([0,1,2,3,'a','b']) = 0. Again, Even - Odd = 2 - 2 = 0. Ignore letters. 
```

The input will be an array of lowercase letters and numbers only. 

In some languages (Haskell, C++, and others), input will be an array of strings:

```
solve ["0","1","2","3","a","b"] = 0 
```

Good luck!

If you like this Kata, please try: 

[Longest vowel chain](https://www.codewars.com/kata/59c5f4e9d751df43cf000035)

[Word values](https://www.codewars.com/kata/598d91785d4ce3ec4f000018)
"""

def count_even_odd_difference(arr):
    # Initialize counters for even and odd numbers
    even_count = 0
    odd_count = 0
    
    # Iterate through the array
    for v in arr:
        # Check if the element is an integer
        if isinstance(v, int):
            # Increment even_count if the number is even, otherwise increment odd_count
            if v % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    
    # Return the difference between even and odd counts
    return even_count - odd_count