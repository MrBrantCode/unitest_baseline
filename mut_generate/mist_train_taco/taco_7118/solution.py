"""
QUESTION:
Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

Chef has $N$ dishes, numbered $1$ through $N$. For each valid $i$, dish $i$ is described by a string $D_{i}$ containing only lowercase vowels, i.e. characters 'a', 'e', 'i', 'o', 'u'.

A *meal* consists of exactly two dishes. Preparing a meal from dishes $i$ and $j$ ($i \neq j$) means concatenating the strings $D_{i}$ and $D_{j}$ in an arbitrary order into a string $M$ describing the meal. Chef *likes* this meal if the string $M$ contains each lowercase vowel at least once.

Now, Chef is wondering - what is the total number of (unordered) pairs of dishes such that he likes the meal prepared from these dishes?

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains a single integer $N$.
$N$ lines follow. For each valid $i$, the $i$-th of these lines contains a single string $D_{i}$.

------  Output ------
For each test case, print a single line containing one integer - the number of ways to prepare a meal Chef likes.

------  Constraints ------
$1 ≤ T ≤ 1,000$
$1 ≤ N ≤ 10^{5}$
$1 ≤ |D_{i}| ≤ 1,000$ for each valid $i$
the sum of all |D_{i}| over all test cases does not exceed $3 \cdot 10^{7}$

------  Subtasks ------
Subtask #1 (20 points):
$1 ≤ T ≤ 100$
$1 ≤ N ≤ 100$
the sum of all |D_{i}| over all test cases does not exceed $20000$

Subtask #2 (80 points): original constraints

----- Sample Input 1 ------ 
1

3

aaooaoaooa

uiieieiieieuuu

aeioooeeiiaiei
----- Sample Output 1 ------ 
2
----- explanation 1 ------ 
Example case 1: There are three possible meals:
- A meal prepared from dishes $1$ and $2$ (for example "aaooaoaooauiieieiieieuuu") contains all vowels.
- A meal prepared from dishes $1$ and $3$ (for example "aaooaoaooaaeioooeeiiaiei") does not contain 'u'.
- A meal prepared from dishes $2$ and $3$ (for example "uiieieiieieuuuaeioooeeiiaiei") contains all vowels.
"""

def count_liked_meals(test_cases):
    def bit_dishes(str_dishes):
        dishes = [0] * 32
        (a, e, i, o, u) = (1, 1 << 1, 1 << 2, 1 << 3, 1 << 4)
        for str_dish in str_dishes:
            dish = 0
            for c in str_dish:
                if c == 'a':
                    dish |= a
                elif c == 'e':
                    dish |= e
                elif c == 'i':
                    dish |= i
                elif c == 'o':
                    dish |= o
                elif c == 'u':
                    dish |= u
                if dish == 31:
                    break
            dishes[dish] += 1
        return dishes

    def count_good(dishes):
        res = 0
        for i in range(1, 32):
            for j in range(i + 1, 32):
                if i | j == 31:
                    res += dishes[i] * dishes[j]
        res += dishes[31] * (dishes[31] - 1) // 2
        return res

    results = []
    for dishes in test_cases:
        dishes_bit_counts = bit_dishes(dishes)
        liked_meals_count = count_good(dishes_bit_counts)
        results.append(liked_meals_count)
    
    return results