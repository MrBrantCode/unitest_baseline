"""
QUESTION:
Implement a function `binary_to_decimal` that takes a list of binary strings, converts each string into its decimal equivalent, and returns a list containing the sum of all decimal numbers and the respective individual decimal numbers. The function should handle exceptions such as non-binary strings, non-string inputs, and an empty list.
"""

def binary_to_decimal(bin_list):
    dec_list = []
    try:
        for bin_num in bin_list:
            try:
                if set(bin_num).issubset('01'):    # Checks if the string is a binary number
                    decimal = int(bin_num, 2)      # Convert binary to decimal
                    dec_list.append(decimal)       # Store the decimal number in the list
                else:
                    print(f"'{bin_num}' is not a valid binary number.")
            except TypeError:
                print(f"{bin_num} is of incorrect type. Only strings representing binary numbers are accepted.")
        if not dec_list: # Edge case: if the input list was empty or contained only non-binary strings
            print("There were no valid binary numbers to convert.")
        else:
            dec_list.insert(0, sum(dec_list))
    except TypeError:
        print("The input is not a list.")
    return dec_list