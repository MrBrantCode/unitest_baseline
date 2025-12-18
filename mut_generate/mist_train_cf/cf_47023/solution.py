"""
QUESTION:
Find a function `find_trio(arr, target)` that takes a sorted or unsorted array of integers `arr` and a target product `target` as input, and returns a trio of numbers from `arr` that, when multiplied together, yield the `target` product. If no such trio exists, return "No solution found". Note that there might be multiple valid solutions, and the function should return one of them.
"""

def find_trio(arr, target):
    arr.sort()
    n = len(arr)

    for i in range(0, n-2):
        start = i + 1
        end = n - 1
        while start < end:
            prod = arr[i]*arr[start]*arr[end]

            # Check if product is smaller, then increment the lower index
            if prod < target:
                start += 1
            # Check if product is greater, then decrement the higher index
            elif prod > target:
                end -= 1
            # If product is equal to target, return trio
            else:
               return (arr[i], arr[start], arr[end])

    return "No solution found"