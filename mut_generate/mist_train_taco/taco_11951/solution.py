"""
QUESTION:
An array is defined to be `inertial`if the following conditions hold:
```
a. it contains at least one odd value  
b. the maximum value in the array is even 
c. every odd value is greater than every even value that is not the maximum value.
```
eg:-
```
So [11, 4, 20, 9, 2, 8] is inertial because 
a. it contains at least one odd value [11,9] 
b. the maximum value in the array is 20 which is even 
c. the two odd values (11 and 9) are greater than all the even values that are not equal to 20 (the maximum), i.e., [4, 2, 8]
```
Write a function called `is_inertial` that accepts an integer array and returns `true` if the array is inertial; otherwise it returns `false`.
"""

def is_inertial(arr):
    # Find the maximum value in the array
    mx = max(arr, default=1)
    
    # Find the minimum odd value in the array
    miO = min((x for x in arr if x % 2 == 1), default=float('-inf'))
    
    # Find the maximum even value that is not the maximum value
    miE2 = max((x for x in arr if x % 2 == 0 and x != mx), default=float('-inf'))
    
    # Check the conditions for the array to be inertial
    return mx % 2 == 0 and miE2 < miO