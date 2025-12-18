"""
QUESTION:
On a weekend, Qingshan suggests that she and her friend Daniel go hiking. Unfortunately, they are busy high school students, so they can only go hiking on scratch paper.

A permutation $p$ is written from left to right on the paper. First Qingshan chooses an integer index $x$ ($1\le x\le n$) and tells it to Daniel. After that, Daniel chooses another integer index $y$ ($1\le y\le n$, $y \ne x$).

The game progresses turn by turn and as usual, Qingshan moves first. The rules follow:

If it is Qingshan's turn, Qingshan must change $x$ to such an index $x'$ that $1\le x'\le n$, $|x'-x|=1$, $x'\ne y$, and $p_{x'}<p_x$ at the same time.

If it is Daniel's turn, Daniel must change $y$ to such an index $y'$ that $1\le y'\le n$, $|y'-y|=1$, $y'\ne x$, and $p_{y'}>p_y$ at the same time.

The person who can't make her or his move loses, and the other wins. You, as Qingshan's fan, are asked to calculate the number of possible $x$ to make Qingshan win in the case both players play optimally.


-----Input-----

The first line contains a single integer $n$ ($2\le n\le 10^5$) — the length of the permutation.

The second line contains $n$ distinct integers $p_1,p_2,\dots,p_n$ ($1\le p_i\le n$) — the permutation.


-----Output-----

Print the number of possible values of $x$ that Qingshan can choose to make her win.


-----Examples-----

Input
5
1 2 5 4 3
Output
1
Input
7
1 2 4 6 5 3 7
Output
0


-----Note-----

In the first test case, Qingshan can only choose $x=3$ to win, so the answer is $1$.

In the second test case, if Qingshan will choose $x=4$, Daniel can choose $y=1$. In the first turn (Qingshan's) Qingshan chooses $x'=3$ and changes $x$ to $3$. In the second turn (Daniel's) Daniel chooses $y'=2$ and changes $y$ to $2$. Qingshan can't choose $x'=2$ because $y=2$ at this time. Then Qingshan loses.
"""

def count_winning_indices(n, nums):
    left = [0] * n
    right = [0] * n
    
    # Calculate left and right arrays
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            left[i] = left[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if nums[i] > nums[i + 1]:
            right[i] = right[i + 1] + 1
    
    # Find the maximum values in left and right arrays
    ml = max(left)
    mr = max(right)
    
    # If the maximum values are not equal, Qingshan cannot win
    if ml != mr:
        return 0
    
    # Count the occurrences of the maximum values
    mlc = left.count(ml)
    mrc = right.count(mr)
    
    # If there are exactly two occurrences of the maximum values, check the condition
    if mlc + mrc == 2:
        for p in range(n):
            if right[p] == mr and left[p] == ml and (not ml % 2):
                return 1
    
    # Default return value if no winning condition is met
    return 0