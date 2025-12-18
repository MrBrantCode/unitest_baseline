"""
QUESTION:
Stannis borathean is attacking kings landing from three gates.To defend the city Tyrion again comes up with a fair solution. Tyrion has N soldier troops with given strengths. Tyrion wants to divide army into 3 sets such that the sum of strengths in these three sets are as equal as possible. In other words he wants to make three sums S1, S2 and S3 using all troops with constraint that  S1 ≥ S2 ≥ S3  and S1 is as less as possible.

Input
Input contains integer  N   which is number of troops followed by N lines. Each line contains an integer, strength of one of the troop.

Output
Strength of strongest set that is sum S1.

Constraints:
1 ≤ N ≤ 12
1 ≤ Strength of each troop ≤ 100

SAMPLE INPUT
4
3
4
1
3

SAMPLE OUTPUT
4

Explanation

The numbers can be divided into three sets S1, S2 and S3 following the condition S1 ≥ S2 ≥ S3 if S1=4, S2=4 and S3=3. Hence the answer is S1=4
"""

def minimize_strongest_set(troops):
    n = len(troops)
    s_v = [999999, 999999, 999999]
    
    def update(a, b):
        nonlocal s_v
        temp = [0, 0, 0]
        for e in range(len(a)):
            temp[b[e]] += a[e]
        if temp[0] >= temp[1] and temp[1] >= temp[2] and temp[0] < s_v[0]:
            s_v = temp
    
    def find(a, b, curr=0):
        if curr == len(a):
            update(a, b)
        else:
            for e in range(3):
                b[curr] = e
                find(a, b, curr + 1)
    
    arr2 = [1] * n
    find(troops, arr2)
    return s_v[0]