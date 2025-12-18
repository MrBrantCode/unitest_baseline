"""
QUESTION:
Write a function called `extract_phone_numbers` that takes a string as input and returns the sum of the last 7 digits of all phone numbers in the string. The function should be able to handle phone numbers in the following formats: +1-XXX-XXX-XXXX, +44 XXX XXX XXXX, 0XXXX XXXXXX, (XXX) XXX-XXXX. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the string.
"""

def extract_phone_numbers(string):
    sum = 0
    i = 0
    while i < len(string):
        if string[i].isdigit():
            i += 1
            continue
        if string[i:i+2] == "+1" or string[i:i+2] == "+4":
            phone_number = ""
            for j in range(i, i+14):
                if string[j].isdigit():
                    phone_number += string[j]
                elif string[j] == "-":
                    continue
                else:
                    break
            if len(phone_number) >= 7:
                sum += int(phone_number[-7:])
            i += 14
        elif string[i] == "(":
            phone_number = ""
            for j in range(i+1, i+14):
                if string[j].isdigit():
                    phone_number += string[j]
                elif string[j] == ")":
                    continue
                else:
                    break
            if len(phone_number) >= 7:
                sum += int(phone_number[-7:])
            i += 14
        else:
            i += 1
    return sum