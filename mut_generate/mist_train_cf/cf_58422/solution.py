"""
QUESTION:
Create a function called `swap_elements` that takes a multidimensional array as input and swaps all even-indexed elements with their respective odd-indexed elements in each sublist. If a sublist has an odd number of elements, the last element should remain in its place. The function should handle potential errors or exceptions and return the modified array.
"""

def swap_elements(arr):
    try:
        # Iterate over all sublists in the array
        for sub_list in arr:
            
            # If sublist has odd number of elements, ignoring the last element
            for i in range(len(sub_list) - len(sub_list) % 2):
                # Swapping odd-indexed and even-indexed elements
                if i % 2 == 0:
                    sub_list[i], sub_list[i + 1] = sub_list[i + 1], sub_list[i]
        
        return arr

    # Handling errors or exceptions
    except Exception as e:
        print(f"An error occurred: {e}")