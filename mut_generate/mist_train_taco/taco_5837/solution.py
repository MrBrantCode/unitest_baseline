"""
QUESTION:
I: Ravage

Santa Claus was caught in the illuminations of the city and broke it.

There are N light bulbs in the illumination, and the $ i $ th light bulb only comes on when the voltage is above $ A_i $ and below $ B_i $.

The voltage should be the same everywhere in the illumination.

Find out how many light bulbs can be lit at the same time by adjusting the voltage.

input

The integer $ N $ is given on the first line.

Of the following $ N $ lines, $ A_i and B_i $ are given on the $ i $ line, separated by blanks.

output

Output the maximum number of light bulbs that can be illuminated at the same time.

Constraint

* $ N $ is an integer greater than or equal to $ 1 $ and less than or equal to $ 100 \ 000 $
* $ A_1, A_2, A_3, \ dots, A_N $ are integers greater than or equal to $ 1 $ and less than or equal to $ 1 \ 000 \ 000 \ 000 $
* $ B_1, B_2, B_3, \ dots, B_N $ are integers greater than or equal to $ 1 $ and less than or equal to $ 1 \ 000 \ 000 \ 000 $
* Satisfy $ A_i \ leq B_i $ for all light bulbs $ i $



Input example 1


Four
14
3 6
2 7
5 8


Output example 1


3


When the voltage is $ 5 $ or $ 3.14 $, there are $ 3 $ bulbs.

Input example 2


2
1 2
twenty three


Output example 2


2






Example

Input

4
1 4
3 6
2 7
5 8


Output

3
"""

def max_illuminated_bulbs(N, ranges):
    """
    Calculate the maximum number of light bulbs that can be illuminated at the same time by adjusting the voltage.

    Parameters:
    N (int): The number of light bulbs.
    ranges (list of tuples): A list of tuples where each tuple (A_i, B_i) represents the voltage range for the i-th light bulb.

    Returns:
    int: The maximum number of light bulbs that can be illuminated at the same time.
    """
    events = []
    for a, b in ranges:
        events.extend([(a, 1), (b + 1, -1)])
    events.sort()
    
    count = 0
    max_count = 0
    for _, v in events:
        count += v
        max_count = max(max_count, count)
    
    return max_count