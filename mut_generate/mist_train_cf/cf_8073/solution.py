"""
QUESTION:
Create a function called `isValidPhoneNumber` that takes a string as input and returns a boolean indicating whether the string represents a valid US phone number. A valid phone number must match the format "(XXX) XXX-XXXX" with the following constraints: 

- The first digit of the area code cannot be 0 or 1.
- The second digit of the area code cannot be 9.
- The three digits of the area code cannot be consecutive or the same.
- The first digit of the phone number cannot be 0 or 1.
- The second digit of the phone number cannot be 9.
- The four digits after the hyphen cannot be consecutive or the same.
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
    
    if areaCode[0] == areaCode[1] == areaCode[2]:
        return False
    
    if int(areaCode) in [int(areaCode[0]) + 1, int(areaCode[0]) - 1, int(areaCode[0]) + 2, int(areaCode[0]) - 2]:
        return False
    
    if phoneNumber[6] in ['0', '1']:
        return False
    
    if phoneNumber[7] == '9':
        return False
    
    if phoneNumber[10] == phoneNumber[11] == phoneNumber[12] == phoneNumber[13]:
        return False
    
    if int(phoneNumber[10:14]) in [int(phoneNumber[10:14][0]) + 1, int(phoneNumber[10:14][0]) - 1, int(phoneNumber[10:14][0]) + 2, int(phoneNumber[10:14][0]) - 2]:
        return False
    
    return True