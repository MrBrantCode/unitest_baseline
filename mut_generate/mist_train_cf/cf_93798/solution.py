"""
QUESTION:
Create a function called `custom_sort` that takes a list of strings as input and sorts them in descending order based on the sum of the ASCII values of their characters. In case of a tie, the strings should be sorted lexicographically. The function should have a time complexity of O(nlogn) and should not use any built-in sorting functions.
"""

def custom_sort(strings):
    def ascii_sum(string):
        return sum(ord(char) for char in string)
    
    def compare_strings(string1, string2):
        sum1 = ascii_sum(string1)
        sum2 = ascii_sum(string2)
        
        if sum1 > sum2:
            return -1  
        elif sum1 < sum2:
            return 1   
        else:
            if string1 < string2:
                return -1  
            elif string1 > string2:
                return 1   
            else:
                return 0   
                
    strings.sort(key=lambda x: (-ascii_sum(x), x))
    return strings