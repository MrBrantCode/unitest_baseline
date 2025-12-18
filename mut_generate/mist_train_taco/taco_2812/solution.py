"""
QUESTION:
Read problems statements in Mandarin Chinese and Russian as well. 

There are N+1 lights. Lights are placed at  (0, 0), (1, 0), (2, 0) ... (N, 0). Initially all the lights are on. You want to turn off all of them one after one.  You want to follow a special pattern in turning off the lights. 

You will start at (0, 0). First, you walk to the right most light that is on, turn it off. Then you walk to the left most light that is on, turn it off. Then again to the right most light that is on and so on. You will stop after turning off all lights. You want to know how much distance you walked in the process. Note that distance between (a,0) and (b,0) is |a-b|.

------ Input ------ 

The first line of the input contains an integer T denoting the number of test cases. Each test case has a single integer N on separate line.

------ Output ------ 

For each test case, output the distance you walked.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}
$$1 ≤ N ≤ 10^{5}

----- Sample Input 1 ------ 
2
1
2
----- Sample Output 1 ------ 
2
5
----- explanation 1 ------ 
Testcase #2
You are initially at (0, 0)
Right most on-light is (2, 0). Distance = 2.
Now you are at (2, 0).
Left most on-light is (0, 0). Distance = 2.
Now you are at (0, 0)
Right most on-light is (1, 0). Distance = 1.
Now you are at (1, 0) and all lights are turned off.
Total distance walked = 5.
"""

def calculate_total_distance(n: int) -> int:
    """
    Calculate the total distance walked to turn off all lights in a special pattern.

    Parameters:
    n (int): The number of lights (N).

    Returns:
    int: The total distance walked.
    """
    if n == 1:
        return 2
    
    left = 0
    right = n
    
    # Calculate the initial distance to the rightmost light
    initial_distance = abs(right - left)
    
    # Calculate the remaining distance using the large distance calculation
    remaining_distance = calculate_large(left, right - 1)
    
    # Total distance is the sum of the initial distance and the remaining distance
    total_distance = initial_distance * 2 + remaining_distance
    
    return total_distance

def calculate_large(left: int, right: int) -> int:
    """
    Helper function to calculate the large distance component.

    Parameters:
    left (int): The leftmost position.
    right (int): The rightmost position.

    Returns:
    int: The calculated large distance.
    """
    d1 = abs(right - left)
    left = left + 1
    d2 = abs(right - left)
    dist = d1 + d2
    first_term = dist % 4
    d = 4
    last_term = dist
    number_n = int((last_term - first_term) / 4 + 1)
    final_sum = number_n / 2 * (last_term + first_term)
    return int(final_sum)