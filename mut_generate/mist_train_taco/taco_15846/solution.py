"""
QUESTION:
On the Internet shopping site, on the same page as the product that the user is currently viewing, some other products that other users have bought in the past along with the product that they are currently viewing are displayed. It is believed that sales can be increased by presenting products that are considered to be highly relevant.

Similar things can be seen in local supermarkets (such as bread and jam) as a way to place items that are often bought together nearby. Your job is to write a program that will help you devise product placement. This time, I would like to set a certain standard number of times and find a combination of two products for which the number of times bought together is equal to or greater than the standard number of times.

When given the information of the products bought together and the standard number of times, create a program that outputs the combination of the two products bought together more than the standard number of times.



Input

The input is given in the following format.


N F
info1
info2
::
infoN


The first line gives the number of pieces of information N (1 ≤ N ≤ 100) and the reference number F (1 ≤ F ≤ 100) of the items bought together. The following N lines are given information on the products bought together. Information about the products bought together infoi is given in the following format.


M item1 item2 ... itemM


M (1 ≤ M ≤ 10) indicates how many products this information contains. itemj is the name of the item bought in this purchase and is a string of 1 to 30 length consisting of only lowercase letters. The same product is never given in infoi.

Output

The number of combinations of two products bought together more than the reference number of times is output on the first line, and all combinations are output on the second and subsequent lines. However, if there is no combination, nothing is output after the second line.

The output order is as follows after arranging the product names in the combination in the lexicographic order (the order in which the words are arranged in the English-Japanese dictionary).

* Compare the first product names, and the one with the earliest in lexicographic order comes first.
* If they are the same, compare the second product names and the lexicographic order comes first.



Separate product names with a single space, and separate product combinations with a single line break.

Examples

Input

5 2
3 bread milk banana
2 milk cornflakes
3 potato bread milk
4 cornflakes bread milk butter
2 potato bread


Output

3
bread milk
bread potato
cornflakes milk


Input

5 5
3 bread milk banana
2 milk cornflakes
3 potato bread milk
4 cornflakes bread milk butter
2 potato bread


Output

0
"""

def find_frequent_product_pairs(N, F, data):
    from collections import defaultdict
    
    # Dictionary to count pairs
    pair_count = defaultdict(int)
    
    # Process each transaction
    for transaction in data:
        M = int(transaction[0])
        items = transaction[1:]
        for i in range(M - 1):
            for j in range(i + 1, M):
                a, b = sorted((items[i], items[j]))
                pair_count[(a, b)] += 1
    
    # Collect pairs that meet the frequency threshold
    frequent_pairs = [(a, b) for (a, b), count in pair_count.items() if count >= F]
    
    # Sort the pairs lexicographically
    frequent_pairs.sort()
    
    # Return the count and the sorted pairs
    return len(frequent_pairs), frequent_pairs