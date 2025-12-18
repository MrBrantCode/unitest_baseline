"""
QUESTION:
Valera had two bags of potatoes, the first of these bags contains x (x ≥ 1) potatoes, and the second — y (y ≥ 1) potatoes. Valera — very scattered boy, so the first bag of potatoes (it contains x potatoes) Valera lost. Valera remembers that the total amount of potatoes (x + y) in the two bags, firstly, was not gerater than n, and, secondly, was divisible by k.

Help Valera to determine how many potatoes could be in the first bag. Print all such possible numbers in ascending order.


-----Input-----

The first line of input contains three integers y, k, n (1 ≤ y, k, n ≤ 10^9; $\frac{n}{k}$  ≤ 10^5).


-----Output-----

Print the list of whitespace-separated integers — all possible values of x in ascending order. You should print each possible value of x exactly once.

If there are no such values of x print a single integer -1.


-----Examples-----
Input
10 1 10

Output
-1

Input
10 6 40

Output
2 8 14 20 26
"""

def find_possible_potatoes(y, k, n):
    # Calculate the remainder when n is divided by k
    l1 = n % k
    # Adjust n to be a multiple of k
    n -= l1
    # Calculate the maximum possible value for x
    t = n - y
    
    # If t is 0 or y is greater than or equal to n, no valid x exists
    if t <= 0 or y >= n:
        return [-1]
    
    # Initialize an empty list to store possible values of x
    possible_x_values = []
    
    # Iterate from t down to 1, decrementing by k each time
    for i in range(t, 0, -k):
        possible_x_values.append(i)
    
    # Return the list of possible values in ascending order
    return possible_x_values[::-1]