"""
QUESTION:
Your task is to create a function called ```sum_arrays()``` in Python or ```addArrays``` in Javascript, which takes two arrays consisting of integers, and returns the sum of those two arrays.

The twist is that (for example) ```[3,2,9]``` does not equal ``` 3 + 2 + 9```, it would equal ```'3' + '2' + '9'``` converted to an integer for this kata, meaning it would equal ```329```. The output should be an array of the the sum  in a similar fashion to the input (for example, if the sum is ```341```, you would return ```[3,4,1]```). Examples are given below of what two arrays should return.
```python
[3,2,9],[1,2] --> [3,4,1]
[4,7,3],[1,2,3] --> [5,9,6]
[1],[5,7,6] --> [5,7,7]
```
If both arrays are empty, return an empty array.

In some cases, there will be an array containing a negative number as the first index in the array. In this case treat the whole number as a negative number. See below:
```python
[3,2,6,6],[-7,2,2,8] --> [-3,9,6,2] # 3266 + (-7228) = -3962
```
"""

def sum_arrays(arr1, arr2):
    # Check if both arrays are empty
    if not arr1 and not arr2:
        return []
    
    # Handle cases where one of the arrays is empty
    if not arr1:
        return arr2
    if not arr2:
        return arr1
    
    # Convert arrays to integers
    def array_to_int(arr):
        if arr[0] < 0:
            return -int(''.join(map(str, arr[1:])))
        return int(''.join(map(str, arr)))
    
    int1 = array_to_int(arr1)
    int2 = array_to_int(arr2)
    
    # Calculate the sum
    total = int1 + int2
    
    # Convert the sum back to an array of digits
    total_str = str(abs(total))
    result = [int(char) for char in total_str]
    
    # Handle negative result
    if total < 0:
        result[0] *= -1
    
    return result