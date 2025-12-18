"""
QUESTION:
You have an integer sequence of length N: a_1, a_2, ..., a_N.
You repeatedly perform the following operation until the length of the sequence becomes 1:
 - First, choose an element of the sequence.
 - If that element is at either end of the sequence, delete the element.
 - If that element is not at either end of the sequence, replace the element with the sum of the two elements that are adjacent to it. Then, delete those two elements.
You would like to maximize the final element that remains in the sequence.
Find the maximum possible value of the final element, and the way to achieve it.

-----Constraints-----
 - All input values are integers.
 - 2 \leq N \leq 1000
 - |a_i| \leq 10^9

-----Input-----
Input is given from Standard Input in the following format:
N
a_1 a_2 ... a_N

-----Output-----
 - In the first line, print the maximum possible value of the final element in the sequence.
 - In the second line, print the number of operations that you perform.
 - In the (2+i)-th line, if the element chosen in the i-th operation is the x-th element from the left in the sequence at that moment, print x.
 - If there are multiple ways to achieve the maximum value of the final element, any of them may be printed.

-----Sample Input-----
5
1 4 3 7 5

-----Sample Output-----
11
3
1
4
2

The sequence would change as follows:
 - After the first operation: 4, 3, 7, 5
 - After the second operation: 4, 3, 7
 - After the third operation: 11(4+7)
"""

def maximize_final_element(N, a):
    # Convert the sequence into a list of tuples (value, index)
    a = [(int(v), i) for (i, v) in enumerate(a)]
    
    # Calculate sums of positive elements at odd and even indices
    ao = sum([v for (v, i) in a if i % 2 and v > 0])
    ae = sum([v for (v, i) in a if not i % 2 and v > 0])
    
    # Determine the maximum possible final element
    if max(ao, ae) == 0:
        ai = a.index(max(a))
        Ans = [1] * ai + list(range(N - ai, 1, -1))
        max_final_element = max(a)[0]
        num_operations = len(Ans)
        operations = Ans
    else:
        if ao >= ae:
            max_final_element = ao
            yn = [i for (v, i) in a if i % 2 and v > 0]
        else:
            max_final_element = ae
            yn = [i for (v, i) in a if not i % 2 and v > 0]
        
        listyn = [i in yn for i in range(N)]
        Ans = []
        
        # Perform operations to reduce the sequence
        while not listyn[0]:
            Ans.append(1)
            listyn = listyn[1:]
        while not listyn[-1]:
            Ans.append(len(listyn))
            listyn = listyn[:-1]
        while True:
            if len(listyn) == 1:
                break
            if len(listyn) == 2 or len(listyn) == 3:
                Ans.append(2)
                break
            if listyn[2]:
                Ans.append(2)
                listyn = [True] + listyn[3:]
            else:
                Ans.append(3)
                listyn = [True, False] + listyn[4:]
        
        num_operations = len(Ans)
        operations = Ans
    
    return max_final_element, num_operations, operations