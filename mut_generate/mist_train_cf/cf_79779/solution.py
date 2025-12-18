"""
QUESTION:
Write a function `find_dyads(arr, target)` that takes an array of integers `arr` and a target sum `target` as input and returns all distinct pairs of numbers in the array that add up to the target sum, minimizing the reuse of array elements in the output pairs.
"""

def find_dyads(arr, target):
    # Initialize empty set
    dyads = set()
    seen = set()
    arr.sort()

    # Iterate through elements in list
    for i in range(len(arr)):
        # If element has been seen before, skip
        if arr[i] in seen:
            continue
        # Calculate the complement that would yield the target sum
        complement = target - arr[i]

        # If complement is present and pair hasn't been added already (avoiding duplication)
        for j in range(i+1, len(arr)):
            if arr[j] == complement and (complement, arr[i]) not in dyads:
                # Add the pair to the set
                dyads.add((arr[i], complement))
                seen.add(arr[i])
                seen.add(complement)
                break

    # Convert the set to a list and return
    return list(dyads)