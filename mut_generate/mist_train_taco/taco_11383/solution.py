"""
QUESTION:
Verma has got 2 arrays of integer numbers. He wished to find the sum of product of all numbers in first array with all the
numbers in second array. 

i.e suppose 1st array A[] contains N numbers and 2nd array B[] contains m numbers.
He wished to calculate for all 1 ≤ i ≤ N and for all 1 ≤ j ≤ M.. sum(Ai*Bi).

As he is busy watching NARUTO. He seeks your help in finding this.

Input Format
1^st line contains 2 space separated integers N and M.
2^nd line contains N space separated integers Ai. 
3^rd line contains M space separated integers Bi. 
Output Format 
1 single line containing only the required answer.

Constraints

1 ≤ N,M ≤ 10^5
-1000 ≤ Ai, Bi ≤ 1000

Problem Setter : Sanchit Bhushan  
Problem Tester :  Pranjul Dubey 

SAMPLE INPUT
2 2
1 2
3 4

SAMPLE OUTPUT
21

Explanation

Here answer is 
31 + 32 + 41 + 42
"""

def calculate_sum_of_products(array_A, array_B):
    """
    Calculates the sum of the product of all numbers in array_A with all numbers in array_B.

    Parameters:
    array_A (list of int): The first array of integers.
    array_B (list of int): The second array of integers.

    Returns:
    int: The sum of the product of all numbers in array_A with all numbers in array_B.
    """
    sum_A = sum(array_A)
    sum_B = sum(array_B)
    return sum_A * sum_B