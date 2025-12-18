"""
QUESTION:
The member states of the UN are planning to send $2$ people to the moon. They want them to be from different countries.  You will be given a list of pairs of astronaut ID's.  Each pair is made of astronauts from the same country.  Determine how many pairs of astronauts from different countries they can choose from.

Example  

$n=4$ 

$astronaut=[1,2],[2,3]$   

There are $\begin{array}{c}4\end{array}$ astronauts numbered $\mbox{0}$ through $3$.  Astronauts grouped by country are $\left[\mbox{0}\right]$ and $[1,2,3]$.  There are $3$ pairs to choose from: $[0,1],[0,2]$ and $[0,3]$.

Function Description  

Complete the journeyToMoon function in the editor below.    

journeyToMoon has the following parameter(s):  

int n: the number of astronauts  
int astronaut[p][2]: each element $\textit{astronaut}[i]$ is a $2$ element array that represents the ID's of two astronauts from the same country  

Returns 

- int: the number of valid pairs

Input Format

The first line contains two integers $n$ and $\boldsymbol{p}$, the number of astronauts and the number of pairs. 

Each of the next $\boldsymbol{p}$ lines contains $2$ space-separated integers denoting astronaut ID's of two who share the same nationality. 

Constraints

$1\leq n\leq10^5$  
$1\leq p\leq10^4$  

Sample Input 0
5 3
0 1
2 3
0 4

Sample Output 0
6

Explanation 0

Persons numbered $[0,1,4]$ belong to one country, and those numbered $[2,3]$ belong to another. The UN has $\boldsymbol{6}$ ways of choosing a pair:  

$[0,2],[0,3],[1,2],[1,3],[4,2],[4,3]$

Sample Input 1
4 1
0 2

Sample Output 1
5

Explanation 1

Persons numbered $[0,2]$  belong to the same country, but persons $\mbox{1}$ and $3$ don't share countries with anyone else.  The UN has $5$ ways of choosing a pair:

$[0,1],[0,3],[1,2],[1,3],[2,3]$
"""

def count_valid_pairs(n, astronaut):
    astronauts = [-1] * n
    countries = []
    
    for (A, B) in astronaut:
        if astronauts[A] > -1 and astronauts[B] > -1:
            if astronauts[A] != astronauts[B]:
                k = astronauts[B]
                countries[astronauts[A]].extend(countries[k])
                for i in countries[k]:
                    astronauts[i] = astronauts[A]
                countries[k] = []
        elif astronauts[A] > -1 and astronauts[B] == -1:
            astronauts[B] = astronauts[A]
            countries[astronauts[A]].append(B)
        elif astronauts[A] == -1 and astronauts[B] > -1:
            astronauts[A] = astronauts[B]
            countries[astronauts[B]].append(A)
        else:
            astronauts[B] = astronauts[A] = len(countries)
            countries.append([A, B])
    
    x = [len(c) for c in countries if c]
    triangular_number = lambda n: n * (n + 1) // 2
    unpaired = sum((x == -1 for x in astronauts))
    total = triangular_number(unpaired - 1)
    total += unpaired * sum(x)
    
    for i in range(len(x) - 1):
        for j in range(i + 1, len(x)):
            total += x[i] * x[j]
    
    return total