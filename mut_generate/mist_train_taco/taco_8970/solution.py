"""
QUESTION:
Jim has invented a new flying object called HZ42. HZ42 is like a broom and can only fly horizontally, independent of the environment. One day, Jim started his flight from Dubai's highest skyscraper, traveled some distance and landed on another skyscraper of same height! So much fun! But unfortunately, new skyscrapers have been built recently.

Let us describe the problem in one dimensional space. We have in total $N$ skyscrapers aligned from left to right. The $\boldsymbol{i}$^{th} skyscraper has a height of $h_i$. A flying route can be described as $(i,j)$ with $i\neq j$, which means, Jim starts his HZ42 at the top of the skyscraper $\boldsymbol{i}$ and lands on the skyscraper $j$. Since HZ42 can only fly horizontally, Jim will remain at the height $h_i$ only. Thus the path $(i,j)$ can be valid, only if each of the skyscrapers $i,i+1,\ldots,j-1,j$ is not strictly greater than $h_i$ and if the height of the skyscraper he starts from and arrives on have the same height. Formally, $(i,j)$ is valid iff $\nexists k\in[i,j]:h_k>h_i$ and $h_i=h_j$.

Help Jim in counting the number of valid paths represented by ordered pairs $(i,j)$.  

Input Format

The first line contains $N$, the number of skyscrapers. The next line contains $N$ space separated integers representing the heights of the skyscrapers. 

Output Format

Print an integer that denotes the number of valid routes.

Constraints

$1\leq N\leq3\cdot10^5$ and no skyscraper will have height greater than $10^{6}$ and less than $\mbox{1}$.

Sample Input #00

6
3 2 1 2 3 3

Sample Output #00

8

Sample Input #01

3
1 1000 1

Sample Output #01

0

Explanation

First testcase: (1, 5), (1, 6) (5, 6) and (2, 4) and the routes in the opposite directions are the only valid routes. 

Second testcase: (1, 3) and (3, 1) could have been valid, if there wasn't a big skyscraper with height 1000 between them.
"""

def count_valid_paths(heights):
    n = len(heights)
    if n < 2:
        return 0
    
    # Sort the indices based on the heights
    hhs = sorted(enumerate(heights), key=lambda t: (t[1], t[0]))
    
    # Initialize prev and next arrays
    prev = list(range(-1, n - 1))
    next = list(range(1, n + 1))
    
    (firsti, firsth) = (lasti, lasth) = hhs[0]
    block_len = 1
    s = 0
    
    for (i, h) in hhs[1:]:
        if h == lasth and i == next[lasti]:
            block_len += 1
            lasti = i
        else:
            s += block_len * (block_len - 1)
            (pi, ni) = (prev[firsti], next[lasti])
            if pi >= 0:
                next[pi] = ni
            if ni < n:
                prev[ni] = pi
            (firsti, firsth) = (lasti, lasth) = (i, h)
            block_len = 1
    
    s += block_len * (block_len - 1)
    return s