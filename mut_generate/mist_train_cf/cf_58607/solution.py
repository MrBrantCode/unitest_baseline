"""
QUESTION:
Create a function called `shortest_seq(input_numbers)` that takes a string of digits `input_numbers` as input and returns the shortest contiguous sequence of digits that contains every unique digit in `input_numbers`. The function should return the shortest sequence as a string. The input string only contains digits and the function should return a contiguous substring of the input string.
"""

def shortest_seq(input_numbers):
    unique_digits = set(input_numbers)
    min_len = len(input_numbers)
    min_seq = input_numbers
  
    i = j = 0
    cur_dict = {}
  
    while j < len(input_numbers):
        if input_numbers[j] not in cur_dict:
            cur_dict[input_numbers[j]] = 1
        else:
            cur_dict[input_numbers[j]] += 1
    
        while len(cur_dict) == len(unique_digits):
            if j-i+1 < min_len:
                min_len = j-i+1
                min_seq = input_numbers[i:j+1]
      
            if cur_dict[input_numbers[i]] == 1:
                del cur_dict[input_numbers[i]]
            else:
                cur_dict[input_numbers[i]] -= 1
            i += 1

        j += 1 
  
    return min_seq