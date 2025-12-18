"""
QUESTION:
There's a waiting room with N chairs set in single row. Chairs are consecutively numbered from 1 to N. First is closest to the entrance (which is exit as well).
 
For some reason people choose a chair in the following way

1. Find a place as far from other people as possible
2. Find a place as close to exit as possible

All chairs must be occupied before the first person will be served

So it looks like this for 10 chairs and 10 patients




Chairs
1
2
3
4
5
6
7
8
9
10




Patients
1
7
5
8
3
9
4
6
10
2




Your task is to find last patient's chair's number. 

Input - N - integer greater than 2 - number of chairs.
Output should positive integer too - last patient's chair's number

Have fun :)
"""

def find_last_patient_chair(n):
    # Ensure the input is valid
    if n <= 2:
        raise ValueError("The number of chairs must be greater than 2.")
    
    # The last patient will always choose the second last chair
    return n - 1