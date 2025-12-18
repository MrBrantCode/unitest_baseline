"""
QUESTION:
Roy lives in a city that is circular in shape on a $2{D}$ plane that has radius ${r}$. The city center is located at origin $(0,0)$ and it has suburbs lying on the lattice points (points with integer coordinates). The city Police Department Headquarters can only protect those suburbs which are located strictly inside the city. The suburbs located on the border of the city are still unprotected. So the police department decides to build at most ${k}}$ additional police stations at some suburbs. Each of these police stations can protect the suburb it is located in.

Given the square of radius, $d(=r^2)$, of the city, Roy has to determine if it is possible to protect all the suburbs.

Input Format 

The first line of input contains integer ${t}}$; ${t}}$ test cases follow. 

Each of the next ${t}}$ lines contains two space-separated integers: ${d}$, the square of the radius of the city, and ${k}$, the maximum number of police stations the headquarters is willing to build.

Constraints 

$1\leq t\leq10^3$ 

$1\leq d\leq2\times10^9$ 

$0\leq k\leq2\times10^9$  

Output Format 

For each test case, print in a new line possible if it is possible to protect all the suburbs;, otherwise, print impossible.

Sample Input

5
1 3
1 4
4 4
25 11
25 12

Sample Output

impossible
possible
possible
impossible
possible

Explanation  

For ${d}=1$, there are ${4}$ points on circumference - [(0,1), (0,-1), (1,0), (-1,0)].
For ${d}=4$, there are ${4}$ points on circumference - [(0,2), (0,-2), (2,0),(-2,0)].
For ${d}=25$, there are $12$ points on circumference - [(0,5), (0,-5), (3,4), (-3,4), (3,-4), (-3,-4), (4,3), (-4,3), (4,-3), (-4,-3), (5,0), (-5,0)].

Test Case #01: There are ${4}$ suburbs on the border, while we are allowed to construct max $k=3$ police stations. 

Test Case #02: We can cover all the ${4}$ suburbs as exactly ${4}$ stations are allowed. 

Test Case #03: We can cover all the ${4}$ suburbs as exactly ${4}$ stations are allowed. 

Test Case #04: It is impossible to cover $12$ suburbs, on the border, with ${11}$ police stations. 

Test Case #05: We can to cover all $12$ suburbs, on the border, with $12$ police stations.  

Timelimits  

Timelimits for this challenge are given here
"""

import math

def can_protect_all_suburbs(d: int, k: int) -> bool:
    """
    Determines if it is possible to protect all suburbs within a circular city with radius r (where d = r^2)
    using at most k additional police stations.

    Parameters:
    d (int): The square of the radius of the city.
    k (int): The maximum number of additional police stations that can be built.

    Returns:
    bool: True if it is possible to protect all suburbs, False otherwise.
    """
    def need(r):
        ret = 0
        if r % 2 == 0 and int(math.sqrt(r // 2)) ** 2 == r // 2:
            ret += 4
        y = int(math.sqrt(r))
        if y * y == r:
            ret += 4
        x = 1
        while True:
            while x < y and x * x + y * y > r:
                y -= 1
            if x >= y:
                break
            if x * x + y * y == r:
                ret += 8
            x += 1
        return ret
    
    return k >= need(d)