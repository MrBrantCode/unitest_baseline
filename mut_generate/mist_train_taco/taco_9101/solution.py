"""
QUESTION:
-----
HALLOWEEN EVE
-----

In some other world, today is Halloween Eve.There are N trees planted in Mr. Smith’s
garden. The height of the i-th tree (1≤i≤N) is h i meters.
He decides to choose K trees from these trees and decorate them with electric lights.
To make the scenery more beautiful, the heights of the decorated trees should be as
close to each other as possible.

	

More specifically, let the height of the tallest decorated tree be hmax meters, and the
height of the shortest decorated tree be hmin meters.
The smaller the value hmax−hmin is, the better. What is the minimum possible value of
hmax−hmin?

		
		

-----Constraints-----

	    2≤K< N ≤105 

1≤hi≤109

hi is an integer
	

-----Input Format-----

Input is given from Standard Input in the following format:

N K 

h1 

h2 

: 

hN

-----Output-----

Print the minimum possible value of hmax−hmin.

		
		

-----Example Text Case-----
Input:

5 3
10
15
11
14
12

Output:

2

Explanation

If we decorate the first, third and fifth trees, hmax=12,hmin=10 so hmax−hmin=2. This is
optimal.
"""

def find_min_height_difference(N, K, heights):
    # Sort the heights list
    heights.sort()
    
    # Initialize a list to store the differences
    diff = []
    
    # Calculate the differences for each possible subset of K trees
    for i in range(N - K + 1):
        diff.append(heights[i + K - 1] - heights[i])
    
    # Return the minimum difference
    return min(diff)