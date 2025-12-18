"""
QUESTION:
A: Information Search

problem

The posting list is a list in which there is a correspondence between the search term and the appearing document ID. For example

* Hokkaido: 1, 2, 4, 9
* Sightseeing: 1, 3, 4, 7



And so on.

From the above posting list, if you search for and, the document with ID 1, 4 will be hit, and if you search for or, ID 1, 2, 3, 4, 7, 9 will be hit.

Here, and search means "listing elements contained in either list", or search means "listing elements contained in at least one of the lists".

Since the posting list is given, output the results of and search and or search respectively.

Input format


n m
a_1 a_2 $ \ ldots $ a_n
b_1 b_2 $ \ ldots $ b_m


All inputs consist of integers.

The first line gives the lengths n and m of the two posting lists to search, separated by spaces.

The second and third lines are given the IDs contained in their respective posting lists, separated by blanks.

Constraint

* 1 \ leq n, m \ leq 2 \ times 10 ^ 5
* a_i <a_j (i <j)
* b_i <b_j (i <j)
* 1 \ leq a_i, b_i \ leq 10 ^ 9



Output format

Let A be the number of hits in the and search, and B be the number of hits in the or search.

Print on the first line in the order A B, separated by blanks.

Output the IDs hit by and search on the following line A in ascending order.

Output the IDs hit by or search on the following B line in ascending order.

Input example 1


4 4
1 2 4 9
1 3 4 7


Output example 1


2 6
1
Four
1
2
3
Four
7
9


Input example 2


4 4
1 3 5 7
2 4 6 8


Output example 2


0 8
1
2
3
Four
Five
6
7
8


Input example 3


3 5
one two Three
1 2 3 4 5


Output example 3


3 5
1
2
3
1
2
3
Four
Five






Example

Input

4 4
1 2 4 9
1 3 4 7


Output

2 6
1
4
1
2
3
4
7
9
"""

def search_posting_lists(n, m, a, b):
    # Convert lists to sets for efficient set operations
    set_a = set(a)
    set_b = set(b)
    
    # Perform AND and OR operations
    and_search_results = sorted(set_a & set_b)
    or_search_results = sorted(set_a | set_b)
    
    # Get the counts of results
    and_search_count = len(and_search_results)
    or_search_count = len(or_search_results)
    
    return and_search_count, or_search_count, and_search_results, or_search_results