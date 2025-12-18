"""
QUESTION:
Implement a function `process_image(temp, BRIGHT_CUTOFF, RED_CUTOFF, GREEN_CUTOFF, BLUE_CUTOFF)` that takes in a 3D array `temp` representing an image and four cutoff values. The function should iterate through the elements of the second dimension of the `temp` array, calculate the average brightness of the RGB values, and check if the individual RGB values are greater than their respective cutoff values. Return a list of elements from the `temp` array where all three RGB values exceed their cutoffs and the average brightness is above the `BRIGHT_CUTOFF` is not a required condition, although it's calculated it's not used.
"""

def process_image(temp, BRIGHT_CUTOFF, RED_CUTOFF, GREEN_CUTOFF, BLUE_CUTOFF):
    result = []
    for row in temp:
        for element in row:
            brightness = sum(element) / 3
            if (element[0] > RED_CUTOFF and 
                element[1] > GREEN_CUTOFF and 
                element[2] > BLUE_CUTOFF):
                result.append(element)
    return result