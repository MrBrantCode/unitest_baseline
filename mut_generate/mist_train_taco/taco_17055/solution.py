"""
QUESTION:
This is an interactive problem.

Note: the XOR-sum of an array a_1, a_2, …, a_n (1 ≤ a_i ≤ 10^9) is defined as a_1 ⊕ a_2 ⊕ … ⊕ a_n, where ⊕ denotes the [bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).

Little Dormi received an array of n integers a_1, a_2, …, a_n for Christmas. However, while playing with it over the winter break, he accidentally dropped it into his XOR machine, and the array got lost.

The XOR machine is currently configured with a query size of k (which you cannot change), and allows you to perform the following type of query: by giving the machine k distinct indices x_1, x_2, …, x_k, it will output a_{x_1} ⊕ a_{x_2} ⊕ … ⊕ a_{x_k}.

As Little Dormi's older brother, you would like to help him recover the XOR-sum of his array a_1, a_2, …, a_n by querying the XOR machine.

Little Dormi isn't very patient, so to be as fast as possible, you must query the XOR machine the minimum number of times to find the XOR-sum of his array. Formally, let d be the minimum number of queries needed to find the XOR-sum of any array of length n with a query size of k. Your program will be accepted if you find the correct XOR-sum in at most d queries.

Lastly, you also noticed that with certain configurations of the machine k and values of n, it may not be possible to recover the XOR-sum of Little Dormi's lost array. If that is the case, you should report it as well.

The array a_1, a_2, …, a_n is fixed before you start querying the XOR machine and does not change with the queries.

Input

The only line of input contains the integers n and k (1 ≤ n ≤ 500, 1 ≤ k ≤ n), the length of the lost array and the configured query size of the XOR machine.

Elements of the original array satisfy 1 ≤ a_i ≤ 10^9.

It can be proven that that if it is possible to recover the XOR sum under the given constraints, it can be done in at most 500 queries. That is, d ≤ 500.

After taking n and k, begin interaction.

Output

If it is impossible to recover the XOR-sum of the array, output -1 immediately after taking n and k. Do not begin interaction.

Otherwise, when your program finds the XOR-sum of the lost array a_1, a_2, …, a_n, report the answer in the following format: "! x", where x is the XOR sum of the array a_1, a_2, …, a_n, and terminate your program normally immediately after flushing the output stream. 

Note that answering does not count as a query.

Interaction

Each query is made in the format "? b", where b is an array of exactly k distinct integers from 1 to n denoting the indices of the elements in the lost array that you want to query the XOR sum of.

You will then receive an integer x, the XOR sum of the queried elements. It can be proven that 0 ≤ x ≤ 2 ⋅ 10^9 will always be true.

After printing a query do not forget to output end of line and flush the output. Otherwise, you will get Idleness limit exceeded. To do this, use:

  * fflush(stdout) or cout.flush() in C++; 
  * System.out.flush() in Java; 
  * flush(output) in Pascal; 
  * stdout.flush() in Python; 
  * see documentation for other languages.



If at any point you make an invalid query or try to make more than 500 queries (which is the hard limit), the interaction will terminate immediately and give you a Wrong Answer verdict. Note that if you exceed d queries, the interaction will continue normally unless you also exceed the 500 query hard limit, though you will still receive a Wrong Answer verdict either way.

Hacks

To hack a solution, use the following format.

The first line contains the integers n and k (1 ≤ n ≤ 500, 1 ≤ k ≤ n).

The second line contains the the array a_1, a_2, …, a_n (1 ≤ a_i ≤ 10^9).

Examples

Input


5 3

4

0

1


Output


? 1 2 3

? 2 3 5

? 4 1 5

! 7


Input


3 2


Output


-1

Note

In the first example interaction, the array a_1, a_2, …, a_n is 2, 1, 7, 5, 6 and its XOR-sum is 7. 

The first query made asks for indices 1,2,3, so the response is a_1 ⊕ a_2 ⊕ a_3 = 2 ⊕ 1 ⊕ 7 = 4.

The second query made asks for indices 2,3,5, so the response is a_2 ⊕ a_3 ⊕ a_5 = 1 ⊕ 7 ⊕ 6 = 0.

The third query made asks for indices 4,1,5, so the response is a_4 ⊕ a_1 ⊕ a_5 = 5 ⊕ 2 ⊕ 6 = 1. Note that the indices may be output in any order.

Additionally, even though three queries were made in the example interaction, it is just meant to demonstrate the interaction format and does not necessarily represent an optimal strategy.

In the second example interaction, there is no way to recover the XOR-sum of Little Dormi's array no matter what is queried, so the program immediately outputs -1 and exits.
"""

def recover_xor_sum(n, k, query_function):
    if n % 2 == 1 and k % 2 == 0:
        return -1
    elif n % k == 0:
        xor = 0
        curr_idx = 1
        while curr_idx <= n:
            next_idx = curr_idx + k
            xor ^= query_function(list(range(curr_idx, next_idx)))
            curr_idx = next_idx
        return xor
    elif n % 2 != k % 2 and n < 2 * k:
        xor = 0
        curr_idx = 1
        kk = n - k
        while True:
            next_idx = curr_idx + kk
            curr_arr = reverse(n, set(range(curr_idx, next_idx)))
            xor ^= query_function(curr_arr)
            curr_idx = next_idx
            if n - curr_idx + 1 < 2 * kk and (n - curr_idx + 1) % 2 == 0:
                break
        if curr_idx < n:
            arr = list(range(1, kk + 1))
            next_idx = curr_idx + (n - curr_idx + 1) // 2
            curr_arr = list(range(curr_idx, next_idx)) + arr
            curr_arr = reverse(n, set(curr_arr[:kk]))
            xor ^= query_function(curr_arr)
            curr_arr = list(range(next_idx, n + 1)) + arr
            curr_arr = reverse(n, set(curr_arr[:kk]))
            xor ^= query_function(curr_arr)
        return xor
    else:
        xor = 0
        curr_idx = 1
        while True:
            next_idx = curr_idx + k
            xor ^= query_function(list(range(curr_idx, next_idx)))
            curr_idx = next_idx
            if n - curr_idx + 1 < 2 * k and (n - curr_idx + 1) % 2 == 0:
                break
        if curr_idx < n:
            arr = list(range(1, k + 1))
            next_idx = curr_idx + (n - curr_idx + 1) // 2
            curr_arr = list(range(curr_idx, next_idx)) + arr
            xor ^= query_function(curr_arr[:k])
            curr_arr = list(range(next_idx, n + 1)) + arr
            xor ^= query_function(curr_arr[:k])
        return xor

def reverse(n, req):
    return [x for x in range(1, n + 1) if x not in req]