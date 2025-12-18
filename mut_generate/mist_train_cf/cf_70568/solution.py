"""
QUESTION:
Develop a function named `count_reverse_pairs` that takes a list of strings as input and returns the quantity of reversed string pairs within the list. The function must disregard special characters, numerals, and spaces when tallying the reversed string pairs and must not be sensitive to case.
"""

def count_reverse_pairs(lst):
    # Initialize a counter
    count = 0

    # Create a helper function to preprocess the string
    def preprocess(s):
        # Convert to lowercase remove non-alphabetic characters
        return ''.join(e for e in s if e.isalpha()).lower()

    # Preprocess the strings in the list
    lst = [preprocess(s) for s in lst]

    # Now do the comparison 
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            # Compare the reverse of lst[i] with lst[j]
            if lst[i] == lst[j][::-1]:
                count += 1
                
    return count