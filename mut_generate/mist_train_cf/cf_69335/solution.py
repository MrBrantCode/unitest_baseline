"""
QUESTION:
Write a function `divByFive` that takes a list of strings representing binary numbers as input, and returns a list of binary numbers that are divisible by 5. The function should convert each binary number to decimal, check for divisibility by 5, and return the binary numbers that meet the condition in their original form.
"""

def divByFive(binaryList):
    divByFiveList = []
    for numStr in binaryList:
        if(int(numStr, 2) % 5 == 0):
            divByFiveList.append(numStr)
    return divByFiveList