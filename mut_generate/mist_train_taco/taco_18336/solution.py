"""
QUESTION:
You are planning the next FIFA World Cup and you are counting the number of highways that need to be built to connect the cities with the venue. 

Your country has $n$ cities and all cities lie on a single straight road called “Highway Road”. If you want to go from City ${x}$ to City $y$ ( where $x\leq y$ ), you need to go through city $x,x+1,x+2,\cdots,y-1,y$. 

The requirements for the highways are as follows:

All games will be held in the $n^{th}$ city.
New bidirectional roads, called "Super Highways", need to be built such that it is possible to visit the $n^{th}$ city from any other city directly.  

You also have the cost to fulfil the second condition. The engineering team knows that if the length of a Super Highway is ${l}$, then it will cost $l^{k}$, where ${k}}$ is an integer constant.The length of Super Highway between city $\boldsymbol{x}$ and $y$ is $|x-y|$.  

For this problem, you need to find only a rough estimation of the cost, hence, find Total Cost Modulo $1000000009$. 

Input Format

First line will contain a single positive integer ${q}$ denoting the number of queries. Then for each case there will be two positive integers, $n$ and ${k}}$.

Constraints

$1\leq q\leq200$  
$1\leq n\leq10^{18}$  
$1\leq k\leq1000$

Output Format

For each case find the cost to build Super Highways such that it is possible to visit $n^{th}$ city from any other city directly. You have to print this value Modulo $1000000009$.

Sample Input 0
1
4 2

Sample Output 0
13

Explanation 0

There are four cities. We need to build Super Highways that connect city ${1}$ to city ${4}$ and city $2$ to city ${4}$. No need to connect city 3 with city ${4}$ since they are adjacent on “Highway Road”. So cost is $(4-1)^2+(4-2)^2=3^2+2^2=13$.
"""

def calculate_super_highway_cost(n, k):
    modulus = 10 ** 9 + 9
    
    def euclidean_alg(a, b):
        rm1 = a
        sm1 = 1
        tm1 = 0
        r = b
        s = 0
        t = 1
        while r != 0:
            q = rm1 // r
            temp_r = rm1
            temp_s = sm1
            temp_t = tm1
            rm1 = r
            sm1 = s
            tm1 = t
            r = temp_r - q * rm1
            s = temp_s - q * sm1
            t = temp_t - q * tm1
        return (rm1, sm1, tm1)

    def modular_inverse(n, p):
        (r, s, t) = euclidean_alg(n, p)
        return s

    def bernoulli_mod(n, modulus):
        res = []
        A = []
        for m in range(n + 1):
            A.append(modular_inverse(m + 1, modulus))
            for j in range(m, 0, -1):
                A[j - 1] = j * (A[j - 1] - A[j]) % modulus
            res.append(A[0])
        return res

    bern = bernoulli_mod(1001, modulus)

    if n <= 2:
        return 0
    
    ans = 0
    bin = 1
    for j in range(k + 1):
        ans = (ans + bin * bern[j] * pow(n - 1, k + 1 - j, modulus)) % modulus
        bin = bin * (k + 1 - j) * modular_inverse(j + 1, modulus) % modulus
    ans = (ans * modular_inverse(k + 1, modulus) - 1) % modulus
    return ans