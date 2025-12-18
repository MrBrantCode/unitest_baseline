"""
QUESTION:
Write a function named `count_xor_pairs` that takes a list as input. The function should count the number of pairs in the list whose XOR value is odd and return this count along with the pairs. The input list can contain integers and binary strings, and may be nested up to 5 levels deep. The function should handle binary strings by converting them to integers before processing, and should be able to efficiently handle lists of up to 10^6 elements.
"""

def count_xor_pairs(lst):
    def flatten(lst):
        """Flatten a list up to 5 levels deep."""
        for _ in range(5):
            lst = [item for sublist in lst for item in (sublist if isinstance(sublist, list) else [sublist])]
        return lst
    
    def handle_bin_str(lst):
        """Convert any binary string to integer."""
        for i in range(len(lst)):
            if isinstance(lst[i], str) and set(lst[i]) <= {'0', '1'}:
                lst[i] = int(lst[i], 2)
        return lst
      
    lst = flatten(lst)
    lst = handle_bin_str(lst)
    
    evens = [x for x in lst if x % 2 == 0]
    odds = [x for x in lst if x % 2 != 0]
    
    pairs = [(i, j) for i in evens for j in odds]
    
    return len(pairs), pairs