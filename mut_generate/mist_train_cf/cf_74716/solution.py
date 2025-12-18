"""
QUESTION:
Write a function `improvised_filter(input_list, low, high, digits)` that takes a list of string representations of numbers, two range thresholds, and a digit limit. The function should filter the list for valid numbers within the provided range, convert them to floating point format, round the decimal part to the digit limit without using built-in rounding functions, and round equidistant numbers towards zero. The function should return a sorted list of unique valid numbers in ascending order. If the list contains any invalid inputs, return "Error: Invalid Input." If no valid numbers are within the range, return "Error: Out of Range."
"""

def improvised_filter(input_list, low, high, digits):
    valid_nums = set()

    for item in input_list:
        try:
            num = float(item)
            if num < low or num > high:
                return "Error: Out of Range."

            dec_part = num - int(num)
        
            # Handle the numbers equidistant from two integers by rounding towards zero
            dec_part *= 10**digits
            if dec_part < -.5:
                dec_part = int(dec_part - .5)
            elif dec_part > .5:
                dec_part = int(dec_part + .5)
            num = int(num) + dec_part / 10**digits

            valid_nums.add(num)
        except ValueError:
            return "Error: Invalid Input."
            
    if valid_nums:
        return sorted(list(valid_nums))
    else:
        return "Error: Out of Range."