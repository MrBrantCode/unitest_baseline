"""
QUESTION:
Write a function `insert_element(arr, element)` that inserts a given `element` at the beginning of a fixed-length array `arr` of integers, shifting all other elements to the right. If the array is already full (i.e., has 10 elements), remove the oldest element before inserting the new one. The function should keep track of the count of each integer in the array and display the count of each integer after insertion. The array should only store integers between 1 and 100 (inclusive).
"""

def insert_element(arr, element):
    # Remove the oldest element if the array is full
    if len(arr) == 10:
        oldest = arr.pop(0)
        print(f"Removing oldest element: {oldest}")
    
    # Shift all other elements to the right
    arr = [element] + arr

    # Count the occurrences of each integer in the array
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1
    
    # Display the count of each integer after insertion
    print(f"Count of each integer: {counts}")

    return arr