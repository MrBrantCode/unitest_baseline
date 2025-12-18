"""
QUESTION:
Welcome to the exciting class of Professor Manasa. In each lecture she used to play some game while teaching a new concept. Today's topic is Set Theory. For today's game, she had given a set A = {a_{1}, a_{2}, ...a_{N}} of N integers to her students and asked them to play the game as follows.  

At each step of the game she calls a random student and asks him/her to select a non-empty subset from set A such that this subset had not been selected earlier and the sum of subset should be even. This game ends when all possible subsets had been selected. Manasa needs your help in counting the total number of times students can be called assuming each student gives the right answer. While it is given that if two numbers are same in the given set, they have different colors. It means that if a1 = a2, then choosing a1 and choosing a2 will be considered as different sets. 

Note  

Two subsets are different if there exists an element (a_{k}) that is present in one subset but not in other. Let's say set A = {a_{1}, a_{2}, a_{3}} = {2, 2, 3}, then all possible subsets are {}, {a_{1}}, {a_{2}}, {a_{3}}, {a_{1}, a_{2}}, {a_{1}, a_{3}}, {a_{2}, a_{3}}, {a_{1}, a_{2}, a_{3}} which is equivalent to {}, {2}, {2}, {3}, {2, 2}, {2, 3}, {2, 3}, {2, 2, 3}.  

Students can be called multiple times.  

Input Format 

The first line contains an integer N i.e. size of set A. 

Next line will contain N integers, each representing an element of A.  

Output Format 

Print number of time students are called. As this number can be very large you have to print the answer modulo (10^{9} + 7). 

Constraints 

1 ≤ N ≤ 10^{5} 

0 ≤ a_{i} ≤ 10^{4} , where i ∈ [1 .. N]

Sample Input 00  

4
2 4 6 1

Sample Output 00  

7

Sample Input 01  

3
1 2 2

Sample Output 01  

3

Explanation 

There are 7 different ways in which a non-empty subset, with even sum, can be selected, i.e., {2}, {4}, {6}, {2, 4}, {2, 6}, {4, 6}, {2, 4, 6}.

For second sample test case, there are 3 different ways in which a non-empty subset, with even sum, can be selected, i.e., {a_{2}}, {a_{3}}, {a_{2}, a_{3}} which is equivalent to {2}, {2}, {2,2}.
"""

def count_even_sum_subsets(N, A):
    mod = 1000000007
    
    # Count the number of odd and even elements in the set A
    odd = len([x for x in A if x % 2 == 1])
    even = N - odd
    
    # If there are no odd elements, treat it as if there is one odd element
    if odd == 0:
        odd = 1
    
    # Calculate the number of valid subsets
    result = (2 ** (odd - 1) % mod * (2 ** even % mod) - 1) % mod
    
    return result