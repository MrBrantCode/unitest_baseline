"""
QUESTION:
Create a function `isValidPhoneNumber` to determine if a given string contains a valid US phone number. The phone number must be in the format "(XXX) XXX-XXXX" with the additional constraints that the first digit of the area code cannot be 0 or 1, and the second digit of the area code cannot be 9.
"""

def isValidPhoneNumber(phoneNumber):
    if len(phoneNumber) != 14:
        return False
    
    if phoneNumber[0] != '(' or phoneNumber[4] != ')' or phoneNumber[5] != ' ' or phoneNumber[9] != '-':
        return False
    
    areaCode = phoneNumber[1:4]
    if areaCode[0] in ['0', '1']:
        return False
    
    if areaCode[1] == '9':
        return False
    
    for digit in phoneNumber[6:9] + phoneNumber[10:]:
        if not digit.isdigit():
            return False
    
    return True