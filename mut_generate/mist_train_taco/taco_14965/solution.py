"""
QUESTION:
You are an immigration officer in the Kingdom of AtCoder. The document carried by an immigrant has some number of integers written on it, and you need to check whether they meet certain criteria.

According to the regulation, the immigrant should be allowed entry to the kingdom if and only if the following condition is satisfied:

* All even numbers written on the document are divisible by 3 or 5.



If the immigrant should be allowed entry according to the regulation, output `APPROVED`; otherwise, print `DENIED`.

Constraints

* All values in input are integers.
* 1 \leq N \leq 100
* 1 \leq A_i \leq 1000

Input

Input is given from Standard Input in the following format:


N
A_1 A_2 \dots A_N


Output

If the immigrant should be allowed entry according to the regulation, print `APPROVED`; otherwise, print `DENIED`.

Examples

Input

5
6 7 9 10 31


Output

APPROVED


Input

3
28 27 24


Output

DENIED
"""

def check_immigrant_entry(N, A):
    # Check if all even numbers in A are divisible by 3 or 5
    for ai in A:
        if ai % 2 == 0 and not (ai % 3 == 0 or ai % 5 == 0):
            return "DENIED"
    return "APPROVED"