"""
QUESTION:
Divide a list of integers into n sections with equal sums. Implement a function `divide_list(lst, n)` that takes two parameters: `lst` (a list of integers) and `n` (the number of sections). The function should return a list of n sublists, each representing a section with an equal sum. If it's not possible to split the list into n sections with equal sums, return an error message.
"""

def divide_list(lst, n):
    total_sum = sum(lst)
    if total_sum % n != 0:
        return "It's not possible to split the list into 'n' sections with equal sums"
        
    target_sum = total_sum // n
    partitions = []
    current_partition = []
    current_sum = 0
    
    for i in lst:
        if current_sum + i > target_sum:
            return "Cannot create equal partitions with the provided list and 'n'"
            
        elif current_sum + i == target_sum:
            current_partition.append(i)
            partitions.append(current_partition)
            current_partition = []
            current_sum = 0
            
        else:
            current_partition.append(i)
            current_sum = current_sum + i
    
    if len(current_partition) > 0:
        return "Cannot create equal partitions with the provided list and 'n'"
        
    return partitions