"""
QUESTION:
Write a function `sort_strings(strings)` that sorts a list of strings by the sum of the ASCII values of their alphabetic characters in descending order. In case of a tie, the strings should be sorted lexicographically. The function should ignore any non-alphabetic characters when calculating the sum and have a time complexity of O(nlogn).
"""

def sort_strings(strings):
    def get_ascii_sum(string):
        ascii_sum = 0
        for char in string:
            if char.isalpha():
                ascii_sum += ord(char)
        return ascii_sum

    if len(strings) <= 1:
        return strings
    
    mid = len(strings) // 2
    left_half = strings[:mid]
    right_half = strings[mid:]
    
    left_half = sort_strings(left_half)
    right_half = sort_strings(right_half)
    
    merged_arr = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left_half) and right_index < len(right_half):
        if get_ascii_sum(left_half[left_index]) > get_ascii_sum(right_half[right_index]):
            merged_arr.append(left_half[left_index])
            left_index += 1
        elif get_ascii_sum(left_half[left_index]) < get_ascii_sum(right_half[right_index]):
            merged_arr.append(right_half[right_index])
            right_index += 1
        else:
            if left_half[left_index] < right_half[right_index]:
                merged_arr.append(left_half[left_index])
                left_index += 1
            else:
                merged_arr.append(right_half[right_index])
                right_index += 1
    
    while left_index < len(left_half):
        merged_arr.append(left_half[left_index])
        left_index += 1
    
    while right_index < len(right_half):
        merged_arr.append(right_half[right_index])
        right_index += 1
    
    return merged_arr