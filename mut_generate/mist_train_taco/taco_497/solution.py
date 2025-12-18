"""
QUESTION:
Your task is to find the number couple with the greatest difference from a given array of number-couples. 

All number couples will be given as strings and all numbers in them will be positive integers.  

For instance: ['56-23','1-100']; in this case, you should identify '1-100' as the number couple with the greatest difference and return it.

In case there are more than one option, for instance ['1-3','5-7','2-3'], you should identify whichever is first, so in this case '1-3'. 

If there is no difference, like so ['11-11', '344-344'], return false.
"""

def find_greatest_difference_couple(arr):
    if not arr:
        return False
    
    def difference(couple):
        num1, num2 = map(int, couple.split('-'))
        return abs(num1 - num2)
    
    greatest_diff_couple = max(arr, key=difference, default=None)
    
    if greatest_diff_couple and difference(greatest_diff_couple) > 0:
        return greatest_diff_couple
    else:
        return False