"""
QUESTION:
«Bersoft» company is working on a new version of its most popular text editor — Bord 2010. Bord, like many other text editors, should be able to print out multipage documents. A user keys a sequence of the document page numbers that he wants to print out (separates them with a comma, without spaces).

Your task is to write a part of the program, responsible for «standardization» of this sequence. Your program gets the sequence, keyed by the user, as input. The program should output this sequence in format l1-r1,l2-r2,...,lk-rk, where ri + 1 < li + 1 for all i from 1 to k - 1, and li ≤ ri. The new sequence should contain all the page numbers, keyed by the user, and nothing else. If some page number appears in the input sequence several times, its appearances, starting from the second one, should be ignored. If for some element i from the new sequence li = ri, this element should be output as li, and not as «li - li».

For example, sequence 1,2,3,1,1,2,6,6,2 should be output as 1-3,6.

Input

The only line contains the sequence, keyed by the user. The sequence contains at least one and at most 100 positive integer numbers. It's guaranteed, that this sequence consists of positive integer numbers, not exceeding 1000, separated with a comma, doesn't contain any other characters, apart from digits and commas, can't end with a comma, and the numbers don't contain leading zeroes. Also it doesn't start with a comma or contain more than one comma in a row.

Output

Output the sequence in the required format.

Examples

Input

1,2,3,1,1,2,6,6,2


Output

1-3,6


Input

3,2,1


Output

1-3


Input

30,20,10


Output

10,20,30
"""

def standardize_page_sequence(sequence: str) -> str:
    # Convert the input string to a list of integers
    A = [int(num) for num in sequence.split(',')]
    
    # Remove duplicates and sort the list
    s_a = sorted(set(A))
    
    # Initialize variables
    prev = None
    string = ''
    count = 0
    
    # Iterate through the sorted list
    for i in s_a:
        if prev is None:
            # First element
            prev = i
            string += str(prev)
            count += 1
        elif i - (prev + count) == 0:
            # Continuation of the current range
            count += 1
        else:
            # End of the current range
            if count > 1:
                string += '-' + str(prev + count - 1) + ',' + str(i)
            else:
                string += ',' + str(i)
            count = 1
            prev = i
    
    # Finalize the last range if necessary
    if count > 1:
        string += '-' + str(prev + count - 1)
    
    return string