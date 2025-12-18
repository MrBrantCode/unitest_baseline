"""
QUESTION:
Create a function called `isValidPhoneNumber` that determines if a given string contains a valid US phone number. The function should check the following conditions:
- The phone number must be in the format "(XXX) XXX-XXXX".
- The first digit of the area code cannot be 0 or 1.
- The second digit of the area code cannot be 9.
- The three digits of the area code cannot be consecutive (e.g. 123, 321, etc.).
- The three digits of the area code cannot be the same (e.g. 111, 222, etc.).
- The first digit of the phone number cannot be 0 or 1.
- The second digit of the phone number cannot be 9.
- The four digits after the hyphen cannot be consecutive (e.g. 1234, 4321, etc.).
- The four digits after the hyphen cannot be the same (e.g. 1111, 2222, etc.).
Return True if the string contains a valid US phone number, False otherwise.
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