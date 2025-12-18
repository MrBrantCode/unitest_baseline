"""
QUESTION:
Read problems statements in Mandarin chinese, Russian and Vietnamese as well. 

In Chefland the ChefSanta gets a list of what children ask from him every year.
On Christmas Eve, the ChefSanta delivers the presents to the children. This year, after Santa finished delivering all the presents, he realized that he used last year’s list. Now he starts thinking about how he could fix this.
We know that

Santa has an infinite amount of every kind of present at home
Santa's reindeer can fly, so he doesn't need roads
Santa has a bag which has a maximum capacity; this capacity is given
Santa can leave an infinite amount of presents at every child's house at any moment except the end
At the end, the Santa has to go to his house, and every house should contain just the present the child from this house wished for.

Santa would like to minimize the total distance that he needs to travel to fix things. Can you help him?

You are not required to find the optimal solution. However, the better your solution is,
the more you will get points

------ Input ------ 

The first line contains T the number of test cases.
The next lines contain the descriptions of each test case.
The first line of each test case contains five space-separated integers N, G, B, X, Y, where N is the number of children in Chefland, G is the number of different presents, B is Santa's bag volume and X, Y are Santa's house coordinates.
The next line contains G integers P_{1}, ..., P_{G} denoting the volume of each present.
The i-th of the next N lines contains four space-separated integers X_{i}, Y_{i}, K_{i}, L_{i}, where X_{i}, Y_{i} are the coordinates of the i-th child's house, K_{i} is last year's present id and L_{i} is this year's present id.

------ Output ------ 

For each test case (in the order given in the input) the output consists of a sequence of commands for Santa (one command per line).
You can give the following commands to Santa:

0 — end of the communication
1 K — travel to X_{K}, Y_{K}, where K=0 means travel to Santa's house
2 K — put one of the presents of type P_{K} to the bag
3 K — take one of the presents of type P_{K} out from the bag

------ Constraints ------ 

$T = 3$
$N = 500$
$10 ≤ G ≤ 50$
$50 ≤ B ≤ 200$
$1 ≤ P_{i} ≤ 20$
$0 ≤ X, Y, X_{i}, Y_{i}  ≤ 10000$
$1 ≤  K_{i}, L_{i}  ≤ G $
$K_{i} != L_{i}$
$The coordinates of houses of all children and Santa's house are pairwise distinct.

------ Example ------ 

Input:
1
3 3 10 0 0
3 5 7
1 0 2 1 
0 1 3 2
1 1 1 3

Output:
1 1
2 2
1 3
2 1
1 2
3 2
2 3
1 3
3 3
1 1
3 1
1 0
0

------ Explanation: ------ 

start with empty bag from 0, 0

1 1            <--- score: 1

2 2            <--- doesn't affect the score, Santa's bag contains 2

1 3            <--- score: 2

2 1            <--- doesn't affect the score, Santa's bag contains 1, 2

1 2            <--- score: 3

3 2            <--- doesn't affect the score, Santa's bag contains 1

2 3            <--- doesn't affect the score, Santa's bag contains 1, 3

1 3            <--- score: 4

3 3            <--- doesn't affect the score, Santa's bag contains 1

1 1            <--- score: 5

3 1            <--- doesn't affect the score, Santa's bag became empty

1 0            <--- score: 6

0              <--- communication end

Another possible output:

start with empty bag from 0, 0

2 1            <--- doesn't affect the score, Santa's bag contains 1

1 1            <--- score: 1

3 1            <--- doesn't affect the score, Santa's bag became empty

2 2            <--- doesn't affect the score, Santa's bag contains 2

1 2            <--- score: 2.4142

3 2            <--- doesn't affect the score, Santa's bag became empty

2 3            <--- doesn't affect the score, Santa's bag contains 3

1 3            <--- score: 3.4142

3 3            <--- doesn't affect the score, Santa's bag became empty

2 1            <--- doesn't affect the score, Santa's bag contains 3

1 0            <--- score: 4.4142

0              <--- communication end

------ Scoring ------ 

The score for each test case is the (Euclidean) distance traveled by Santa. Your total score will be the sum of your scores over all the test cases in all the test files. There will be 10 official test files. During the contest you will be able to get your score on the first 2 test files. After the contest the score for the full test set will be shown.

------ Test Case Generation ------ 

When we say a number is chosen from (a,b), it means an integer number chosen randomly and uniformly between a and b inclusive.

$T is 3 (except sample)$
$N is 500 $
$G is chosen from (10, 50)$
$B is chosen from (50, 200)$
$Every coordinate is chosen uniquely from (0, 10000).$
$We choose a minP from (1, 5), and maxP from (5, 20). Every P_{i} is chosen from (minP, maxP).$
$For each i, distinct  K_{i} and L_{i}  are chosen from (1, G).$
"""

def optimize_santa_delivery(T, test_cases):
    results = []
    
    for case in test_cases:
        N = case['N']
        G = case['G']
        B = case['B']
        X = case['X']
        Y = case['Y']
        present_volumes = case['present_volumes']
        children_info = case['children_info']
        
        commands = []
        
        for i in range(N):
            (p, q, r, s) = children_info[i]
            commands.append(f"1 {i + 1}")
            commands.append(f"2 {r}")
            commands.append("1 0")
            commands.append(f"3 {r}")
            commands.append(f"2 {s}")
            commands.append(f"1 {i + 1}")
            commands.append(f"3 {s}")
            commands.append("1 0")
        
        commands.append("0")
        results.append(commands)
    
    return results