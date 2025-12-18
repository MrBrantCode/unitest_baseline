"""
QUESTION:
In the city, there are two pastry shops. One shop was very popular because its cakes are pretty tasty. However, there was a man who is displeased at the shop. He was an owner of another shop. Although cause of his shop's unpopularity is incredibly awful taste of its cakes, he never improved it. He was just growing hate, ill, envy, and jealousy.

Finally, he decided to vandalize the rival.

His vandalize is to mess up sales record of cakes. The rival shop sells K kinds of cakes and sales quantity is recorded for each kind. He calculates sum of sales quantities for all pairs of cakes. Getting K(K-1)/2 numbers, then he rearranges them randomly, and replace an original sales record with them.

An owner of the rival shop is bothered. Could you write, at least, a program that finds total sales quantity of all cakes for the pitiful owner?

Constraints

* Judge data contains at most 100 data sets.
* 2 ≤ K ≤ 100
* 0 ≤ ci ≤ 100

Input

Input file contains several data sets. A single data set has following format:


K
c1 c2 ... cK×(K-1)/2


K is an integer that denotes how many kinds of cakes are sold. ci is an integer that denotes a number written on the card.

The end of input is denoted by a case where K = 0. You should output nothing for this case.

Output

For each data set, output the total sales quantity in one line.

Example

Input

2
2
3
5 4 3
0


Output

2
6
"""

def calculate_total_sales(K, sales_pairs):
    """
    Calculate the total sales quantity of all cakes given the sales quantities for all pairs of cakes.

    Parameters:
    - K (int): The number of kinds of cakes.
    - sales_pairs (list of int): A list of integers representing the sales quantities for all pairs of cakes.

    Returns:
    - int: The total sales quantity of all cakes.
    """
    if K == 0:
        return 0
    
    total_sales = sum(sales_pairs)
    return total_sales // (K - 1)