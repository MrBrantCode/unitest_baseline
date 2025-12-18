"""
QUESTION:
Chandan is back with his array to blow your mind. As usual Chandan has an array consisting of N integers .He allows you to perform 2 kinds of operation on his array.

Type 1 : Increment any integer of the array by 1.

Type 2 : Decrement any integer of the array by 1.

You can perform these operation as many times as you want on his array.

Each  operation of Type 1 costs 3 while each operation of Type 2 costs 5.

Now Chandan wants to have K equal elements in his array.So he asks you to tell him the minimum cost required in obtaining K equal elements in his array.

Input:

The first line contains T indicating test cases.Second line contains 2 integers N indicating the number of elements in his array and K.

Third line contains N space separated integers denoting Chandan array.

Output:

The minimum cost required to get K equal elements.

Constraints :

1 ≤ T ≤ 100

1 ≤ K ≤ N ≤100

1 ≤ A[i] ≤100

SAMPLE INPUT
1
5 3
9 4 9 7 4 

SAMPLE OUTPUT
6

Explanation

We can convert 7 to 9 to get three 9. The cost of this conversion will be 6.
"""

def minimum_cost_to_equalize_elements(arr, N, K):
    new_arr = sorted(set(arr))
    new_len = len(new_arr)
    count_arr = []
    cost_arr = [[] for _ in range(105)]
    cost_arr_min = []

    def calculate_cost(i, arr_sent):
        for j in arr_sent:
            r = arr.count(j)
            if i > j:
                diff = i - j
                n = [diff * 3] * r
                cost_arr[i] += n
            else:
                diff = j - i
                n = [diff * 5] * r
                cost_arr[i] += n

    for i in range(new_len):
        j = arr.count(new_arr[i])
        count_arr.append(j)
        j_value = K - j
        j_list = [x for x in new_arr if x != new_arr[i]]
        calculate_cost(new_arr[i], j_list)
        cost = 0
        while j_value > 0:
            cost_arr[new_arr[i]].sort(reverse=True)
            cost += cost_arr[new_arr[i]].pop()
            j_value -= 1
        cost_arr_min.append(cost)

    return min(cost_arr_min)