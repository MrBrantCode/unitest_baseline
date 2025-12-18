"""
QUESTION:
There are $n$ groups of friends, and each group is numbered from 1 to $n$. The ${i}^{th}$ group contains $a_i$ people. 

They live near a bus stop, and only a single bus operates on this route. An empty bus arrives at the bus stop and all the groups want to travel by the bus. 

However,  group of friends do not want to get separated. So they enter the bus only if the bus can carry the entire group. 

Moreover, the groups do not want to change their relative positioning while travelling.  In other words, group 3 cannot travel by bus, unless group 1 and group 2 have either (a) already traveled by the bus in the previous trip or (b) they are also sitting inside the bus at present.

You are given that a bus of size $\boldsymbol{x}$ can carry $\boldsymbol{x}$ people simultaneously. 

Find the size $\boldsymbol{x}$ of the bus so that 
(1) the bus can transport all the groups and 
(2) every time when the bus starts from the bus station, there is no empty space in the bus (i.e. the total number of people present inside the bus is equal to $\boldsymbol{x}$)?

Input Format 

The first line contains an integer $n$ $(1\leq n\leq10^5)$. The second line contains $n$ space-separated integers $a_1,a_2,\ldots,a_n$ $(1\leq a_i\leq10^4)$.

Output Format

Print all possible sizes of the bus in an increasing order.

Sample Input

8
1 2 1 1 1 2 1 3

Sample Output

3 4 6 12

Sample Explanation

In the above example, 
$a_1$ = 1, $a_2$ = 2, $a_3$ = 1, $a_{4}$ = 1, $a_{5}$ = 1, $a_{6}$ = 2, $a_{7}$ = 1, $a_{8}$ = 3.

If x = 1 : 
In the first trip, $a_1$ go by the bus.
There will be no second trip because the bus cannot accommodate group 2. Hence "x = 1" is not the required answer.

If x = 2 :
No bus trip is possible. That's because $a_1$ cannot go alone, as one seat will be left vacant in the bus. And, $a_1$ & $a_2$ cannot go together, because the bus is cannot accommodate both the groups simultaneously.

If x = 3 : 
In the first trip, $a_1$ & $a_2$ go by the bus. 
In the second trip, $a_3$, $a_{4}$ & $a_{5}$ go by the bus. 
In the third trip, $a_{6}$ & $a_{7}$ go by the bus. 
In the fourth trip, $a_{8}$ go by the bus. 

If x = 4 : 
In the first trip, $a_1$, $a_2$ & $a_3$ go by the bus. 
In the second trip,  $a_{4}$, $a_{5}$ & $a_{6}$go by the bus. 
In the third trip, $a_{7}$ & $a_{8}$ go by the bus. 

Similarly you can figure out the output for x= 5, 6 & 7.
"""

def find_bus_sizes(n, group_sizes):
    def min_and_max(array):
        minimum = maximum = array[0]
        for el in array[1:]:
            maximum += el
            if el > minimum:
                minimum = el
        return minimum, maximum

    def multiples_of(begin, n):
        multiples = set()
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                multiples.add(i)
                multiples.add(n // i)
        multiples = [x for x in multiples if x >= begin]
        multiples.sort()
        return multiples

    minimum, maximum = min_and_max(group_sizes)
    possible_values = multiples_of(minimum, maximum)
    count_possible_values = len(possible_values)
    count = [0] * count_possible_values

    for el in group_sizes:
        for i in range(count_possible_values):
            count[i] += el
            if count[i] == possible_values[i]:
                count[i] = 0

    result = [possible_values[i] for i in range(count_possible_values) if count[i] == 0]
    return result