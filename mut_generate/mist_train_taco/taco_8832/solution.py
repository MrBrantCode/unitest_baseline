"""
QUESTION:
There are N piles where the i^{th} pile consists of A_{i} stones.

Chef and Chefina are playing a game taking alternate turns with Chef starting first.  
In his/her turn, a player can choose any non-empty pile and remove exactly 1 stone from it. 

The game ends when exactly 2 piles become empty. The player who made the last move wins.  
Determine the winner if both players play optimally.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of multiple lines of input.
- The first line of each test case contains a single integer N denoting the number of piles.
- Next line contains N space-separated integers A_{1}, A_{2}, \dots, A_{N} - denoting the number of stones in each pile.

------ Output Format ------ 

For each test case, output CHEF if Chef wins the game, otherwise output CHEFINA.

Note that the output is case-insensitive i.e. CHEF, Chef, cHeF, and chef are all considered the same.

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$2 ≤ N ≤ 10^{5}$
$1 ≤ A_{i} ≤ 10^{9}$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^{5}$.

----- Sample Input 1 ------ 
2
2
5 10
3
1 1 3

----- Sample Output 1 ------ 
CHEF
CHEFINA

----- explanation 1 ------ 
Test Case $1$: The game will end when both piles become empty. Thus, the game will last exactly $15$ moves with last move made by Chef.

Test Case $2$: It can be shown that Chefina has a winning strategy.
"""

def determine_winner(T, test_cases):
    results = []
    for tt in range(T):
        N = test_cases[tt][0]
        arr = test_cases[tt][1]
        
        arr1 = arr[:]
        for i in range(3):
            for j in range(N - 1 - i):
                if arr1[j] < arr1[j + 1]:
                    arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]
        
        min1 = arr1[N - 1]
        min2 = arr1[N - 2]
        min3 = arr1[N - 3]
        
        sum_stones = sum(arr)
        cnt1 = arr.count(1)
        cnt2 = arr.count(2)
        
        if cnt1 >= 2:
            if (sum_stones - N) % 2 == 1:
                results.append('CHEF')
            else:
                results.append('CHEFINA')
        elif cnt1 == 1:
            if sum_stones % 2 == 1 or (cnt2 >= 1 and (sum_stones - N) % 2 == 1):
                results.append('CHEF')
            else:
                results.append('CHEFINA')
        elif sum_stones % 2 == 1:
            results.append('CHEF')
        else:
            results.append('CHEFINA')
    
    return results