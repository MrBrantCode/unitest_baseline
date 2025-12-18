"""
QUESTION:
Write a function `three_sum` that takes a list of integers `numbers` and a target integer `target`. The function should return all unique combinations of three numbers in the list that add up to the target number, without including any repeating numbers from the list. The function should be efficient in terms of time and memory space, and should handle invalid inputs gracefully. 

The input list and target should only contain integers. If the input is invalid, the function should return an error message. The function should have a time complexity better than O(n^3) and should be able to handle large input lists.
"""

def three_sum(numbers, target):
    # Validate input
    try:
        numbers = [int(i) for i in numbers]
        target = int(target)
    except ValueError:
        # Handle a non-integer input
        try:
            return f"Error: all list elements and target must be integers, but got {numbers} and {target}."
        except Exception:
            return f"Error: undefined variables were used."  
  
    # Sort the list
    numbers.sort()

    triples = []

    for i in range(len(numbers) - 2):
        if i > 0 and numbers[i] == numbers[i - 1]:
            continue
        l, r = i + 1, len(numbers) - 1
        while l < r:
            s = numbers[i] + numbers[l] + numbers[r]
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                triples.append([numbers[i], numbers[l], numbers[r]])
                while l < r and numbers[l] == numbers[l + 1]:
                    l += 1
                while l < r and numbers[r] == numbers[r - 1]:
                    r -= 1
                l += 1
                r -= 1

    return triples