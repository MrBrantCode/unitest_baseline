"""
QUESTION:
Design a function `five_div_seq(n: int, start: int, end: int)` that generates and counts the number of times the digit 5 appears in decreasing arithmetic sequences that only contain integers less than a provided 'n' and divisible by either 9 or 14. The function should also validate against a given start and end number for the sequences. The function should take three parameters: 'n', 'start', and 'end', and return an integer. The parameters 'n', 'start', and 'end' should be integers.
"""

def five_div_seq(n: int, start: int, end: int) -> int:
    # Initialize the counter
    count = 0
    #Iterate through the range in reverse
    for i in range(n-1, 0, -1):
        #Check if the number is divisible by 9 or 14
        if i % 9 == 0 or i % 14 == 0:
            #Validate if the number falls between start and end
            if start <= i <= end:
                #Calculate the number of times 5 appears in the number
                count += str(i).count('5')
    #Return the counter
    return count