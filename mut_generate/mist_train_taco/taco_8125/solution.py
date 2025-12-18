"""
QUESTION:
It has been truly said that love is not meant for everyone.

Let me introduce you to a very sad story of my friend Broken Amit. Yes several times he has been left heartbroken. Looking at his poor condition even God is pity on him. God has given Amit a very nice opportunity to Kiss as many girls as he likes . 

There are N number of girls each having a "Love value" as well as a decrement value. 
So, Amit needs to kiss all the N girls exactly once in some order.
 In one step, he can kiss only a single girl and after every step girl's "Love value" decreases by an amount equal to her decrement value times her index (indexing starts from 0) .  But once a girl has been kissed her "Love value" won't decrease in further steps. 

"Love value" for Amit in a particular step is equal to the sum of "Love values" of all the n girls before the beginning of that step, whereas the "Gross Love Value" of Broken Amit is sum of  "Love Values" for Amit in each step. 

Now Amit not being a good analyzer wants your help to find the maximum "Gross Love Value" he can earn.
Input

First line contains an integer N - denoting the number of girls.

Second line contains N integers denoting the initial "Love value" of the girls (L[i]).

Third line contains N integers denoting the "decrement value of the girls (D[i]).
Output

Single integer denoting maximum "Gross Love Value", Broken Amit can earn.
Constraints

1 ≤ n ≤ 17

0 ≤ L[i] < 500000

0 ≤ D[i] < 500000

SAMPLE INPUT
2
2 4
1 2

SAMPLE OUTPUT
12

Explanation

If Amit kisses the first girl and then the 2nd one -
1st step - 2 + 4 = 6
2nd step - 2 + (4 - 12) = 4
Gross Love Value - 6+4 = 10
If Amit kisses the 2nd girl than the 1st one. 
1st step - 2 + 4 = 6
2nd step - (2 - 01) + 4 = 6
Gross Love Value = 12
"""

def calculate_max_gross_love_value(N, love_values, decrement_values):
    # Helper function to calculate the sum of love values
    def sum_love_values(lst, n):
        res = 0
        for i in range(n):
            res += lst[i][0]
        return res
    
    # Helper function to update the love values after each step
    def update_love_values(lst, k, n):
        for i in range(k, n):
            lst[i][0] -= (lst[i][1] * lst[i][2])
    
    # Create a list of tuples containing love value, decrement value, and index
    lst = []
    for i in range(N):
        lst.append([love_values[i], decrement_values[i], i])
    
    # Sort the list based on the decrement value times index in descending order
    lst.sort(key=lambda x: -(x[1] * x[2]))
    
    # Calculate the maximum gross love value
    max_gross_love_value = 0
    for i in range(N):
        max_gross_love_value += sum_love_values(lst, N)
        update_love_values(lst, i + 1, N)
    
    return max_gross_love_value