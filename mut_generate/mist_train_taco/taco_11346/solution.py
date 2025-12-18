"""
QUESTION:
Xavier is a computer science student.He is given a task by his teacher the task is to 
generate a code which accepts an array of n integers.He now has to select an integer from this array but there is a trick in selection of integer from the array.
                   For the selection process he first has to accept an integer m less than the size of array,then he has to delete the  mth element from this array,then again he starts counting from the next element after the deleted element in a form of loop like a circular array and deletes the m th element from that position.He continues this process until a single integer remains.
                    Now after he has one integer remaining in that array he has to check whether it is odd or even.If that number is odd than he has to print all odd numbers present in the original array else he has to print all even numbers present in the original array. But the ouput must be in sorted manner.

INPUT:

First line contains integer n for size of array.
Second line inputs the integer array.
third line inputs the value of m.

OUTPUT:

The set of odd or even numbers as per the task.

CONSTRAINTS

3<n<100
1<m<n.

SAMPLE INPUT
6
3 5 7 1 2 8
3

SAMPLE OUTPUT
1 3 5 7

Explanation

The first line inputs no of integer that is 6
The next line has the integer 3,5 7,1,2,8 then 3 is given as input .
so,the third element is deleted now new array is 3,5,1,2,8 now begin from 1 and delete the third element from there so new array is 3,5,1,2.Now the process continues from beginning as the deleted element was the last element of array so we again begin from starting.
This process is continued untill a single no. remains in the array.
"""

def select_and_filter_numbers(n, array, m):
    # Helper function to count the number of active elements in the array
    def noofelement(array):
        return sum(1 for i in range(len(array)) if array[i][1])
    
    # Helper function to get the single remaining value
    def getSingleValue(array):
        for i in range(len(array)):
            if array[i][1]:
                return array[i][0]
    
    # Helper function to get all even numbers from the array
    def getEven(array):
        return sorted(array[i][0] for i in range(len(array)) if array[i][0] % 2 == 0)
    
    # Helper function to get all odd numbers from the array
    def getOdd(array):
        return sorted(array[i][0] for i in range(len(array)) if array[i][0] % 2 != 0)
    
    # Initialize the array with active flags
    a = [[array[i], True] for i in range(n)]
    
    # Perform the deletion process until one element remains
    loop = noofelement(a)
    while loop > 1:
        count = 0
        i = 0
        while i < m:
            if not a[count][1]:
                count += 1
                if count >= len(a):
                    count = 0
                continue
            if i == (m - 1):
                a[count][1] = False
            count += 1
            if count >= len(a):
                count = 0
            i += 1
        loop = noofelement(a)
    
    # Determine the last remaining number
    check = getSingleValue(a)
    
    # Return the appropriate sorted list of numbers
    if check % 2 == 0:
        return getEven(a)
    else:
        return getOdd(a)