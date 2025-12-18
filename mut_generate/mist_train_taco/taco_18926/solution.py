"""
QUESTION:
My flatmate, Sayan, once invited all his relatives and friends from all over the city to join him on his birthday party.
He is also famous for boasting that all his friends and relatives belong to "proper" families.
Now, he appointed a gaurd to allow only his relatives and friends into the party.
It is gauranteed that all the relatives and friends come with their families all at once ,i.e, all members belonging to the same family reach all at once.
Now gaurd's task is to count the number of "proper" families who came in the party.
All families have a unique "special number" assigned to them ,i.e., all members of the same family share the same "special number".
A family is said to be  proper only if the number of members in the familiy is a number which can be made by adding numbers from a given set of "valid" numbers N. Further constraint is that each valid number can be used only once.

Take an example:-

if N={1,2,8}
then all the families with 1,2,3,8,9,10 , or 11 members are allowed in the party , where as families with 4,5,6,7, etc members are not allowed.

The gaurd being a lazy fellow came to you for help.You need to write a program that computes the number of "proper families" in who turned up.

INPUT.

First line of input contains a number T denoting the number of test cases.T test cases follow.
In each test case, the first line contains the number(P) of total number of people coming for the party and the number (M) denoting the number of "valid" numbers.
The 2nd line contains M numbers,  the set N ,containing all distinct "valid" numbers separated with spaces.
The 3rd line contains P numbers, the "special" number of the members separated with spaces.

OUTPUT.

Output a single line for each of the test cases that denotes the number of "proper families" who turned up for the party.

CONSTRAINTS:

1 ≤ T ≤ 5

1 ≤ P,N,M ≤ 1000

SAMPLE INPUT
2
8 3
1 2 8
2 2 2 3 4 4 4 4
10 3
2 4 6
2 9 9 9 19 19 19 19 19 20

SAMPLE OUTPUT
2
0

Explanation

In the first case:
Clearly, The families with 1,2,3,8,9,10 and 11 members are allowed in the party.
The family with "Special" number 2 has 3 members in it which is allowed.Same for the family with "special" number 3.
But for the family with "special" number 4 has 4 members, which is not allowed.
So the total number of "proper" families = 2.
"""

def count_proper_families(T, test_cases):
    def isSumInSubset(inputSet, n, m):
        T = []
        for i in range(0, n+1):
            col = []
            for j in range(0, m+1):
                col.append(False)
            T.append(col)
        for i in range(0,n+1):
            T[i][0] = True
        for i in range(1,m+1):
            T[0][i] = False

        for i in range(1,n+1):
            for j in range(1,m+1):
                if j < inputSet[i-1]:
                    T[i][j] = T[i-1][j]
                else:
                    T[i][j] = T[i-1][j] or T[i-1][j - inputSet[i-1]]

        return T[n]

    results = []
    for case in test_cases:
        p, m, valid_nums, family_ids = case

        family_ids_count = {}
        max_count_from_single_family = 0
        for fid in family_ids:
            if fid in family_ids_count:
                family_ids_count[fid] += 1
            else:
                family_ids_count[fid] = 1
            if max_count_from_single_family < family_ids_count[fid]:
                max_count_from_single_family = family_ids_count[fid]

        count = 0
        T = isSumInSubset(valid_nums, m, max_count_from_single_family)
        for _id in family_ids_count:
            if T[family_ids_count[_id]]:
                count += 1
        results.append(count)
    
    return results