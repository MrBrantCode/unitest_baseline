"""
QUESTION:
A long way back I have taken $5000 from Golu when I used to live in Jodhpur. Now, time has passed and I am out of Jodhpur. While Golu still in Jodhpur, one day called me and asked about his money.
I thought of giving Golu a chance. I told him that he can still take his money back if he reaches my home anyhow just in 2 days but not after that. 
In excitement he made his way toward my hometown i.e. Gorakhpur. To cover up the petrol cost he started giving paid lift to whoever needs it throughout the way in order to earn some money. Help him to get the maximum profit.

His car has a capacity of k + 1 person, so in a certain moment he can transport k persons (and himself). 
From Jodhpur to Gorakhpur, there are l localities (cities, towns, villages), Jodhpur being the first and Gorakhpur being the lth.
There are n groups of lift takers along the road. The ith
group consists of pi persons, wants to travel from locality si  to locality di and will pay an amount of mi money.
A group must be taken into the car as a whole. Assume that lift takers are found only in localities.

Restrictions
• 1 ≤ k ≤ 7
• 1 ≤ l ≤ 1000000
• 1 ≤ n ≤ 50
• 1 ≤ pi ≤ k
• 1 ≤ si ≤ l – 1
• 2 ≤ di ≤ l
• si < di
• 1 ≤ mi ≤ 1000000

-----Input-----
The first line of the input contains the number of test cases.
The first line of each test case contains the numbers n, l and k separated by a single space.
n lines follow, the ith line containing pi, si, di and mi separated by a single space.


-----Output-----
For each test case output a single line containing the maximum amount of money Golu can earn.

-----Example-----
Input:
2
5 5 4
2 1 5 50
1 2 4 20
2 3 4 40
2 4 5 50
3 4 5 80
10 10 5
2 5 10 17300
2 1 8 31300
5 4 10 27600
4 8 10 7000
5 9 10 95900
2 7 10 14000
3 6 10 63800
1 7 10 19300
3 8 10 21400
2 2 10 7000

Output:
140
127200

By:
Chintan, Asad, Ashayam, Akanksha
"""

def calculate_max_profit(n, l, k, groups):
    class Group:
        def __init__(self, size, start, end, value):
            self.size = size
            self.start = start
            self.end = end
            self.value = value

        def __lt__(self, other):
            return self.start < other.start

        def __str__(self):
            return '%i: %i->%i, $%i' % (self.size, self.start, self.end, self.value)

    def hash(car, i):
        people = []
        for group in car:
            people.extend([group.end] * group.size)
        people.sort()
        return tuple(people + [i])

    def optimize(groups, car, capacity, i):
        if i == len(groups):
            return 0
        newcar = []
        pos = groups[i].start
        for group in car:
            if group.end > pos:
                newcar.append(group)
            else:
                capacity += group.size
        state = hash(newcar, i)
        try:
            return memo[state]
        except:
            v = optimize(groups, newcar, capacity, i + 1)
            if groups[i].size <= capacity:
                w = optimize(groups, newcar + [groups[i]], capacity - groups[i].size, i + 1) + groups[i].value
            else:
                w = 0
            if v > w:
                ie[state] = -1
            elif v < w:
                ie[state] = 1
            else:
                ie[state] = 0
            ans = max(v, w)
            memo[state] = ans
            return ans

    memo = {}
    ie = {}
    group_objects = [Group(pi, si, di, mi) for pi, si, di, mi in groups]
    group_objects.sort()
    return optimize(group_objects, [], k, 0)