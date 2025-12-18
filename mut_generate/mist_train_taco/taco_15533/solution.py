"""
QUESTION:
In this problem your goal is to guess some secret permutation A of integers from 1 to 16.

There are 17 tests in this problem. Test number i  for 1 ≤ i ≤ 16 will have the following form:
the first line of the input contains string "ELEMENT" (without quotes)
the second line of the input of the test i contains two integers from 1 to 16 each - i and element A[i] of the secret permutation
the only line of the output file contains one integer - A[i] too.

Input of the last (the 17-th test) will contain the only string "PERMUTATION" (without quotes). For this test your program should output some permutation of integers from 1 to 16 - your variant of the secret permutation.

If this permutation equals to the secret permuation A and passes all the 17 tests with your solution , you will receive 100 points. Otherwise you will receive 0 points. Note that for each wrong try you will receive 20 minutes penalty time after you solved this problem (as in ACM ICPC format)

Let us remind you that after you submit solution you can see a detailed feedback for each test separately.

 You can't use "compile and test" without using custom input. If you want to test your solution on hackerearth platform , please use custom input. 

SAMPLE INPUT
[EXAMPLE OF POSSIBLE TEST #2]
ELEMENT
2 4

[EXAMPLE OF POSSIBLE TEST #17]
PERMUTATION

SAMPLE OUTPUT
4


3 4 5 6 7 1 8 9 10 11 13 15 16 12 2 14
"""

def guess_permutation(test_type, index=None, element=None):
    # The secret permutation A
    secret_permutation = [13, 15, 1, 6, 14, 4, 5, 7, 2, 16, 9, 11, 10, 12, 8, 3]
    
    if test_type == "ELEMENT":
        if index is None or element is None:
            raise ValueError("Both index and element must be provided for 'ELEMENT' test type.")
        return secret_permutation[index - 1]
    
    elif test_type == "PERMUTATION":
        return secret_permutation
    
    else:
        raise ValueError("Invalid test type. It should be either 'ELEMENT' or 'PERMUTATION'.")