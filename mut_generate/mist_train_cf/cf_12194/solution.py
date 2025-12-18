"""
QUESTION:
Create a function called `find_pair` that takes two inputs: an array of integers `numbers` and an integer `target`. The function should find a pair of elements in the `numbers` array whose sum matches the `target`. If multiple pairs exist, return the pair with the highest sum. If no such pair exists, return an empty array.

The `numbers` array will not exceed 10^5 elements, and the elements will be integers between -10^9 and 10^9. The `target` will also be an integer between -10^9 and 10^9. If there are multiple pairs with the highest sum, any of them can be returned.
"""

def find_pair(numbers, target):
    # Create a hash table to store the difference between each element and the target
    complements = {}
    
    # Iterate through the array
    for num in numbers:
        complement = target - num
        
        # Check if the complement exists in the hash table
        if complement in complements:
            # If the complement exists, we have found a pair
            # Return the pair with the highest sum
            return [max(num, complement), min(num, complement)]
        
        # Add the element to the hash table
        complements[num] = True
    
    # If no pair is found, return an empty array
    return []