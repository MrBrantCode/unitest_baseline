"""
QUESTION:
Create a function `longest_common_substring(list1, list2)` that takes two lists of integers as input and returns the product of their longest common substrings. A longest common substring must be a strictly increasing subsequence with a length of at least 5. If there are multiple longest common substrings with the same length, return the product of the one that starts at the earliest index in `list1`. If there are no common substrings, return -1.
"""

def longest_common_substring(list1, list2):
    # Initialize variables
    max_length = 0
    max_product = -1
    longest_substring = []
    
    # Iterate through the first list
    for i in range(len(list1)):
        # Check if there are enough elements remaining in the first list to form a substring of length 5
        if len(list1) - i < 5:
            break
        
        # Iterate through the second list
        for j in range(len(list2)):
            # Check if there are enough elements remaining in the second list to form a substring of length 5
            if len(list2) - j < 5:
                break
            
            # Check if the current elements in both lists are equal
            if list1[i] == list2[j]:
                # Initialize variables for the current substring
                current_length = 1
                current_product = list1[i]
                current_substring = [list1[i]]
                
                # Iterate through the remaining elements in both lists to find the longest common substring
                k = i + 1
                l = j + 1
                while k < len(list1) and l < len(list2):
                    # Check if the current elements in both lists are equal
                    if list1[k] == list2[l]:
                        current_length += 1
                        current_product *= list1[k]
                        current_substring.append(list1[k])
                    else:
                        # Check if the current substring is longer than the previous longest substring
                        if current_length >= 5 and current_length > max_length:
                            max_length = current_length
                            max_product = current_product
                            longest_substring = current_substring
                        break
                    k += 1
                    l += 1
                
                # Check if the current substring is longer than the previous longest substring
                if current_length >= 5 and current_length > max_length:
                    max_length = current_length
                    max_product = current_product
                    longest_substring = current_substring
    
    # Check if a longest common substring was found
    if max_product != -1:
        return max_product
    else:
        return -1