"""
QUESTION:
The chef was not happy with the binary number system, so he designed a new machine which is having 6 different states, i.e. in binary there is a total of 2 states as 0 and 1. Now, the chef is confused about how to correlate this machine to get an interaction with Integer numbers, when N(Integer number) is provided to the system, what will be the Nth number that system will return(in Integer form), help the chef to design this system.

-----Input:-----
- First-line will contain $T$, the number of test cases. Then the test cases follow. 
- Each test case contains a single line of input, $N$. 

-----Output:-----
For each test case, output in a single line answer given by the system.

-----Constraints-----
- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$

-----Sample Input:-----
2
3
5

-----Sample Output:-----
7
37

-----EXPLANATION:-----
Initial numbers for system = [1, 6, 7, 36, 37, 42, 43, 216, …..
For 1) 3rd Number for the system will be 7.
For 2) 5th Number for the system will be 37.
"""

def get_nth_system_number(N: int) -> int:
    # Precomputed list of system numbers
    system_numbers = [1, 6, 7]
    c = 1
    
    # Generate the system numbers up to the required size
    for x in range(3, 100001):
        if x % 2 == 1:
            a = system_numbers[c] * 6
            system_numbers.append(a)
        else:
            system_numbers.append(a + 1)
            c += 1
    
    # Return the Nth system number (1-based index)
    return system_numbers[N - 1]