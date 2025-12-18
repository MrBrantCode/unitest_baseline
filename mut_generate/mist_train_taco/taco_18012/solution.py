"""
QUESTION:
This is an interactive problem. You have to use flush operation right after printing each line. For example, in C++ you should use function fflush(stdout), in Java — System.out.flush(), in Pascal — flush(output) and in Python — sys.stdout.flush().

In this problem, you need to find maximal and minimal elements of an array. What could be simpler?

You can imagine that the jury has an array, and initially you know the only number n — array's length.

Array's elements are numbered from 1 to n. You are allowed to compare two elements of the array by using their indices i and j. There are three possible responses to this query: '<' (if ai is less than aj), '=' (if ai is equal to aj) and finally '>' (if ai is greater than aj).

It's known that it's always possible to find both maximal and minimal elements of the array by using no more than <image> comparisons, where ⌈ x⌉ is the result of rounding x up.

Write the program that will find positions of the minimum and the maximum in the jury's array of length n, by using no more than f(n) comparisons.

Interaction

Each test for this problem will contain one or more arrays. You have to find positions of minimal and maximal elements for each of these arrays. The first line of the input contains integer T (1 ≤ T ≤ 1000) — number of arrays in the test.

Thus, at the beginning, you program should read number T, and then it should solve the problem for T jury's arrays one by one.

Then input for each array goes. Firstly, your program has to read the number n (1 ≤ n ≤ 50) — the length of the array. It will be provided in the next line of the input.

Further, your program can perform comparisons or report that the answer is found.

  * To perform a comparison, you have to output string of the following pattern «? i j» (i and j must be integer numbers from 1 to n) — the indices of the elements to compare in the current query. 
  * To report the indices of minimal and maximal elements of the hidden array, your program have to output a line in the form «! i j» (i and j must be integer numbers from 1 to n), where i is an index of the minimal element of array, and j is an index of the maximal element of the array. If there are several possible answers to the problem, you can output any of them. 



There are several possible responses for a comparison:

  * '<' — if ai is less than aj, 
  * '=' — if ai is equal to aj, 
  * '>' — if ai is greater than aj. 



For an array of length n your program can make at most <image> comparisons. Note that the operation of reporting an answer («! i j» ) is not included into the value of f(n).

After the answer is reported, your program has to solve the problem for the next array or it should terminate if all T arrays are processed.

Example

Input

2
2
 
&gt;
 
3
 
=
 
=
 

Output

 
 
? 1 2
 
! 2 1
 
? 3 1
 
? 2 1
 
! 2 3
"""

def find_min_max_indices(n, compare_func):
    Max_a = []
    Min_a = []
    a = range(n)
    
    for i in range(int(n / 2)):
        if compare_func(i * 2, i * 2 + 1) == '>':
            Max_a.append(i * 2)
            Min_a.append(i * 2 + 1)
        else:
            Max_a.append(i * 2 + 1)
            Min_a.append(i * 2)
    
    if n % 2 == 1:
        Max_a.append(n - 1)
        Min_a.append(n - 1)
    
    Max_index = Max_a[-1]
    Min_index = Min_a[-1]
    
    for i in range(len(Max_a) - 1):
        if compare_func(Max_a[i], Max_index) == '>':
            Max_index = Max_a[i]
    
    for i in range(len(Min_a) - 1):
        if compare_func(Min_a[i], Min_index) == '<':
            Min_index = Min_a[i]
    
    return Min_index, Max_index