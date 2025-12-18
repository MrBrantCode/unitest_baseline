"""
QUESTION:
You have been speeding on a motorway and a police car had to stop you. The policeman is a funny guy that likes to play games. Before issuing penalty charge notice he gives you a choice to change your penalty. 

Your penalty charge is a combination of numbers like: speed of your car, speed limit in the area, speed of the police car chasing you, the number of police cars involved, etc.  So, your task is to combine the given numbers and make the penalty charge to be as small as possible.      

For example, if  you are given numbers  ```[45, 30, 50, 1]``` your best choice is ```1304550```


Examples:
```Python
['45', '30', '50', '1'] => '1304550'

['100', '10', '1'] => '100101'

['32', '3'] => '323'
```
"""

def minimize_penalty(numbers):
    # Convert all numbers to strings
    str_numbers = list(map(str, numbers))
    
    # Find the maximum length of the string representations of the numbers
    max_len = max(map(len, str_numbers))
    
    # Sort the numbers based on a custom key that ensures the smallest combination
    sorted_numbers = sorted(str_numbers, key=lambda s: s.ljust(max_len, s[-1]))
    
    # Join the sorted numbers to form the smallest penalty charge
    return ''.join(sorted_numbers)