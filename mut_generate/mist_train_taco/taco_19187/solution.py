"""
QUESTION:
problem

You are a traveler traveling on the JOI Highway. The JOI Highway is a road that extends straight from east to west, and there are n post towns on the JOI Highway. Numbered. The westernmost post town on the JOI highway is post town 1, and the easternmost post town is post town n.

You have decided to depart from post town 1 and embark on an m-day journey. Your itinerary is determined according to the sequence a1, a2, ..., am as follows. It is a non-zero integer that represents how to move the eyes. If the post town you depart on day i is post town k, then on day i you move straight from post town k to post town k + ai. Means to do.

The number of post towns n, the number of days of travel m, the information on the distance between post towns, and the sequence a1, a2, ... Create a program that finds the remainder by dividing the sum by 100000 = 105.

Diagram corresponding to the input / output example

<image>

output

The output consists of one line containing the remainder of your total distance traveled in the m-day journey divided by 100000 = 105.

Input / output example

Input example 1


7 5
2
1
1
3
2
1
2
-1
3
2
-3


Output example 1


18


On the first day you move from post town 1 to post town 3. On the second day you move from post town 3 to post town 2. And on the third day you move from post town 2 to post town 5. Move, move from post town 5 to post town 7 on the 4th day, move from post town 7 to post town 4 on the 5th day. Your total travel distance in a 5-day trip is 18.

The above question sentences and the data used for the automatic referee are the question sentences created and published by the Japan Committee for Information Olympics and the test data for scoring.



input

The integers n and m are separated by blanks on the first line. N (2 ≤ n ≤ 100000 = 105) is the number of post towns on the JOI highway, and m (1 ≤ m ≤ 100000 = 105) is Represents the number of days of travel.

The following n − 1 line represents the distance between post towns on the JOI highway. I + 1st line (1 ≤ i ≤ n − 1) is a positive integer si that represents the distance between post town i and post town i + 1. (1 ≤ si ≤ 100) is written.

The following m line contains a sequence of movements for m days. Line i + n (1 ≤ i ≤ m) contains a non-zero integer ai that represents your movement method for day i. Has been.

In the scoring data, it does not move west of post town 1 or east of post town n.

Of the scoring data, 50% of the points are satisfied with n ≤ 100 and m ≤ 100.

Example

Input

7 5
2
1
1
3
2
1
2
-1
3
2
-3


Output

18
"""

def calculate_travel_distance(n, m, distances, movements):
    # Calculate the cumulative distances
    accums = [0]
    for distance in distances:
        accums.append(accums[-1] + distance)
    
    # Initialize the result and starting position
    result = 0
    k = 0
    
    # Calculate the total travel distance
    for movement in movements:
        result = (result + abs(accums[k + movement] - accums[k])) % 100000
        k += movement
    
    return result