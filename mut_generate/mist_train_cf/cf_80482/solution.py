"""
QUESTION:
Create a function `int_to_mayan(num)` that converts an integer into its corresponding Mayan numeral representation. The Mayan numeral system uses a dot to represent 1 and a bar to represent 5. The function should handle inputs that are not valid integers or are outside the Mayan numeral system's range of 0-19.
"""

def int_to_mayan(num):
    # Dictionaries to store mayan representation of numbers
    dots_and_bars = {1:'.', 2:'..', 3:'...', 4:'....', 5:'-', 6:'-.', 7:'--.', 8:'--..',
                      9:'--...', 10:'--....', 11:'---.', 12:'---..', 13:'---...', 14:'---....', 
                      15:'----', 16:'-----', 17:'------', 18:'-------', 19:'--------'}

    zero_representation = "0" # Can substitute with the actual Mayan zero representation

    try:
        num = int(num) # Convert value to int
        if num < 0: # If value is negative
          return "Negative integers can't be represented in Mayan Numerals."
        elif num == 0: # If value is zero
          return zero_representation
        elif num > 19: # If value is > 19
          return "Numbers beyond 19 can't be represented in Simple Mayan Numerals."

        return dots_and_bars[num] # Return the Mayan representation

    except ValueError: 
        return "Invalid integer."