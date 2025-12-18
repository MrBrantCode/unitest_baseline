"""
QUESTION:
Create a function named `convert_to_hex` that takes an integer as input and returns its hexadecimal equivalent as a string. The input number should be a three-digit positive integer between 100 and 999, inclusive. The function should not use any built-in conversion functions or libraries. If the input number is outside the valid range, return the error message "Invalid input! Please enter a three-digit number."
"""

def convert_to_hex(num):
    # Define a dictionary to map decimal numbers to hexadecimal characters
    hex_dict = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
        10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
    }
    
    # Check if the input number is within the valid range (100 to 999)
    if num < 100 or num > 999:
        return "Invalid input! Please enter a three-digit number."
    
    # Divide the number by 16^2 (256) to get the most significant digit
    msd = num // 256
    
    # Get the remaining number after extracting the most significant digit
    remaining = num % 256
    
    # Divide the remaining number by 16 to get the middle digit
    middle_digit = remaining // 16
    
    # Get the least significant digit by taking the remainder after dividing by 16
    lsd = remaining % 16
    
    # Convert each digit to hexadecimal using the dictionary
    hex_msd = hex_dict[msd]
    hex_middle = hex_dict[middle_digit]
    hex_lsd = hex_dict[lsd]
    
    # Return the hexadecimal equivalent as a string
    return hex_msd + hex_middle + hex_lsd