"""
QUESTION:
Princess'Marriage

Marriage of a princess

English text is not available in this practice contest.

A brave princess in a poor country, knowing that gambling payouts are determined by the parimutuel method, felt more familiar with gambling and was convinced of her victory in gambling. As a result, he spent more money than ever before and lost enough to lose all the taxes paid by the people. The King, who took this situation seriously, decided to marry the princess to the neighboring country. By doing this, I thought that I would like the princess to reflect on her daily activities and at the same time deepen her friendship with neighboring countries and receive financial assistance.

The princess and the prince of the neighboring country liked each other, and the kings of both countries agreed on a political marriage. The princess triumphantly went to the neighboring country with a little money in her hand. On the other hand, the motive for the princess to marry is to pursue the unilateral interests of the king, and the aide of the prince of the neighboring country who thinks that it is not pleasant shoots countless thugs along the way to make the princess dead. It was.

The path the princess will take has already been decided. There are a total of L post stations on the path of the princess. For convenience, the departure and arrival points are also set as post stations, and each post station is called S1, S2, ... SL. The princess shall be in S1 first, visit the post station in ascending order (S2, S3 ... in that order), and finally go to SL. At the post station, you can pay money to hire an escort, and as long as you have the money, you can contract for as long as you like to protect the princess. The cost of hiring an escort is 1 gold per distance. Note that the princess can also partially protect the section through which she passes. The distance between Si and Si + 1 is given by Di, and the expected value of the number of times a thug is attacked per distance between Si and Si + 1 is given by Pi.

Find the expected number of thugs to reach your destination when the princess has a budget of M and hires an escort to minimize the expected number of thugs.

Input

The input consists of multiple datasets. Each dataset has the following format.

> N M
> D1 P1
> D2 P2
> ...
> DN PN

Two integers are given in the first row of each dataset, representing the number of intervals N (1 ≤ N ≤ 10,000) and the budget M (0 ≤ M ≤ 1,000,000,000) of the princess difference, respectively. The next N lines show information about the path the princess takes. Each line contains two integers, and the i-th line is the expected value of the interval Di (1 ≤ Di ≤ 10,000) and the number of attacks when moving one unit distance between them Pi (0 ≤ Pi <= 10) ). The end of the input is represented by a data set with N = 0 and M = 0. Do not output the calculation result for this data set.

Output

For each dataset, output the expected number of times the princess will be attacked by thugs to your destination.

Sample Input


2 8
5 6
4 5
3 1
5 10
5 10
5 10
0 0


Output for the Sample Input


Five
140






Example

Input

2 8
5 6
4 5
3 1
5 10
5 10
5 10
0 0


Output

5
140
"""

def calculate_expected_attacks(N, M, intervals):
    if N == 0 and M == 0:
        return 0
    
    # Calculate the total expected attacks without any protection
    total_expected_attacks = sum(Di * Pi for Di, Pi in intervals)
    
    # Sort intervals by the cost-effectiveness of protection (Pi / Di) in descending order
    intervals.sort(key=lambda x: x[1] / x[0], reverse=True)
    
    # Apply the budget to minimize the expected attacks
    for Di, Pi in intervals:
        if M >= Di:
            total_expected_attacks -= Di * Pi
            M -= Di
        elif M > 0:
            total_expected_attacks -= M * Pi
            M = 0
        if M == 0:
            break
    
    return total_expected_attacks