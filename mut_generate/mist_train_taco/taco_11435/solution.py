"""
QUESTION:
There is an event in DUCS where boys get a chance to show off their skills to impress girls. The boy who impresses the maximum number of girls will be honoured with the title “Charming Boy of the year”.
There are $N$ girls in the department. Each girl gives the name of a boy who impressed her the most. You need to find the name of a boy who will be honoured with the title. 
If there are more than one possible winners, then the one with the lexicographically smallest name is given the title. 
It is guaranteed that each boy participating in the event has a unique name.

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows. 
- The first line of each test case contains an integer $N$ denoting the number of girls.
- The second line contains $N$ space-separated strings $S_1, S_2, \ldots, S_N$, denoting the respective names given by the girls.

-----Output-----
For each test case, print a single line containing a string — the name of the boy who impressed the maximum number of girls. In case of a tie, print the lexicographically smallest name.

-----Constraints-----
- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $1 \leq |S_i| \leq 10$, for each valid $i$
$(|S_i|$ is the length of the string $S_i)$
- For each valid $i$, $S_i$ contains only lowercase English alphabets
- Sum of $N$ over all the test cases is $\leq 10^6$

-----Subtasks-----
- 30 points: $1 \leq N \leq 100$
- 70 points: original constraints

-----Sample Input-----
2

10

john berry berry thomas thomas john john berry thomas john

4

ramesh suresh suresh ramesh   

-----Sample Output-----
john

ramesh
"""

from collections import Counter

def find_charming_boy(test_cases):
    results = []
    
    for case in test_cases:
        N, names = case
        name_count = Counter(names)
        
        # Find the maximum count of impressions
        max_count = max(name_count.values())
        
        # Collect all names with the maximum count
        top_names = [name for name, count in name_count.items() if count == max_count]
        
        # Sort the names lexicographically and select the smallest
        top_names.sort()
        results.append(top_names[0])
    
    return results