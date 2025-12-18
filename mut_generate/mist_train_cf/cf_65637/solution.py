"""
QUESTION:
Create a function `find_swap_pairs(sequence)` that returns a dictionary containing the highest index of an element which is not greater or equal to the previous element and the index of the next smaller element that can be swapped with it to potentially correct the sequence. The function should return {'index': -1, 'swap_with': -1} if there is no such element. The input sequence will not contain duplicate values.
"""

def find_swap_pairs(sequence):
    if not sequence or len(sequence) < 2:
        return {'index': -1, 'swap_with': -1}
    
    index = -1
    swap_with = -1
    
    for i in range(len(sequence) - 1):
        if sequence[i] > sequence[i + 1]:
            index = i + 1
            temp_swap_with = -1
            
            for j in range(i, -1, -1):
                if sequence[j] < sequence[index]:
                    temp_swap_with = j
                    break
            if temp_swap_with != -1:
                swap_with = temp_swap_with
                break
    
    return {'index': index, 'swap_with': swap_with}