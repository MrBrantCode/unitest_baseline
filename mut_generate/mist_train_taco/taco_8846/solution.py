"""
QUESTION:
It is said that a legendary treasure left by Mr. Yao is sleeping somewhere in Hachioji long ago. The treasure map, which is said to show its whereabouts, has been handed down by Yao's n descendants, divided into several pieces.

Now, the descendants of Mr. Yao were trying to cooperate to obtain the treasure. However, the treasure cannot be found only by a part of the treasure map that points to the location of the treasure. Therefore, all the descendants of Mr. Yao gathered and tried to collect the map in one place. However, even if I tried to put it into practice, I couldn't get together because I couldn't meet the schedule. However, this information about the treasure is valuable information that has been secretly passed down in the clan. Considering the risk of leakage, exchanging maps using public communication means is out of the question.

Therefore, I decided to collect the map for one descendant by repeating the process of meeting the descendants in person and handing over the map. There is no limit to the number of people that one person can meet in a day, but it is necessary that there is a schedule for each other.

Your job is to write a program that asks for at least how many days it will take to collect a map from a list of open days on schedule for each offspring.

By the way, the unity of the Yao clan is very tight. If the descendants who finally get the entire map betray the other descendants and take away the treasure, they will be sanctioned by the clan. The sanctions are so horrifying that it is virtually impossible for their descendants to actually carry away the treasure.



Input

The input consists of multiple datasets.

Each dataset consists of multiple rows. The first line contains the integer n (1 <n <= 50), which represents the number of people with a piece of the map. The next n lines contain the schedule for each descendant. Line i represents the schedule of the i-th descendant, with some integers separated by a single character space. The first integer fi (0 <= fi <= 30) is an integer that represents the number of days that the descendant's schedule is free. The following fi integers represent dates when the schedule is free. These dates differ from each other and are all greater than or equal to 1 and less than or equal to 30.

There is one line containing only 0 at the end of the input.

Output

Print one integer on one line for each dataset. If you can collect the map within 30 days, output the minimum number of days required to collect the map, otherwise output -1.

Addendum: The above "minimum number of days required to collect maps" means the date when all maps are collected earliest starting from one day.

Example

Input

4
1 1
2 2 3
2 1 2
3 3 4 5
0


Output

3
"""

def find_minimum_days_to_collect_maps(n, schedules):
    days = [[] for _ in range(31)]
    
    for i in range(n):
        hima = schedules[i]
        for d in hima[1:]:
            days[d].append(i)
    
    tos = [{i} for i in range(n)]
    end = {i for i in range(n)}
    
    for i in range(1, 31):
        gather = set()
        for to in days[i]:
            gather = gather | tos[to]
        if gather == end:
            return i
        for to in days[i]:
            tos[to] = gather
    
    return -1