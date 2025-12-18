"""
QUESTION:
Create a function called `binary_representation` that takes an integer `start_number` as input. The function should return a dictionary where the keys are the numbers from `start_number` down to 0 (or up to 0 if `start_number` is negative), and the values are the binary representations of the corresponding keys. Ensure that the binary representation of negative numbers is handled correctly, showing only the binary digits without any prefix or sign.
"""

def binary_representation(start_number):
    counter_dict = {}
    if start_number > 0:
        while start_number>=0:
            counter_dict[start_number] = bin(start_number)[2:] 
            start_number-=1
    else:
        while start_number<=0:
            counter_dict[start_number] = bin(start_number & 0xffffffff)[2:] 
            start_number+=1
    return counter_dict