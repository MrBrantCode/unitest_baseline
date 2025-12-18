"""
QUESTION:
Karan likes the number 4 very much.

Impressed by the power of this number, Karan has begun to look for occurrences of four anywhere. He has a list of T integers, for each of them he wants to calculate the number of occurrences of the digit 4 in the decimal representation. He is too busy now, so please help him.

------ Input Format ------ 

The first line of input consists of a single integer T, denoting the number of integers in Karan's list.

Then, there are T lines, each of them contain a single integer from the list.

------ Output Format ------ 

Output T lines. Each of these lines should contain the number of occurrences of the digit 4 in the respective integer from Karan's list.

------ Constraints ------ 

1 ≤ T ≤ 10^{5}
(Subtask 1): 0 ≤ Numbers from the list  ≤ 9 - 33 points.
(Subtask 2): 0 ≤ Numbers from the list  ≤ 109 - 67 points.

----- Sample Input 1 ------ 
5
447474
228
6664
40
81

----- Sample Output 1 ------ 
4
0
1
1
0
"""

def count_digit_four(numbers):
    """
    Counts the occurrences of the digit '4' in each integer from the input list.

    Parameters:
    numbers (list of int or str): A list of integers (or their string representations) for which the digit '4' needs to be counted.

    Returns:
    list of int: A list where each element is the count of the digit '4' in the corresponding input integer.
    """
    return [str(num).count('4') for num in numbers]