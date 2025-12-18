"""
QUESTION:
Chef likes to travel a lot. Every day Chef tries to visit as much cities as possible. Recently he had a quite a few trips of great Chefland for learning various recipes. Chefland had N cities numbered from 1 to N. People in Chefland are very friendly, friendliness of i-th city is given by Fi.

Before starting of each trip, Chef's initial enjoyment is 1 unit. Whenever he visits a city with friendliness Fi, his enjoyment gets multiplied by Fi units. 

City 1 is the home city of Chef. He starts each trip from his home city. Before starting a trip, he chooses a parameter R which denotes that he will start from city 1, and go to city 1 + R, then to 1 + 2 * R, then to 1 + 3 * R, till 1 + i * R such that i is largest integer satisfying 1 + i * R ≤ N.

Now, Chef wants you to help him recreate his visit of the cities. Specifically, he will ask you Q queries, each of which can be of following two types.

- 1 p f : friendliness of p-th city changes to f, i.e. Fp = f 
- 2 R   : Find out the total enjoyment Chef will have during this trip. As Chef does not like big numbers, he just asks you to output two things, first digit of the enjoyment and value of enjoyment modulo 109 + 7.

-----Input-----
There is a single test case.
First line of input contains a single integer N, denoting number of cities in Chefland.
Second line of the input contains N space separated integer - F1, F2, ..., FN, denoting the friendliness of the cities in order from 1 to N.
Next line contains an integer Q, denoting number of queries.

For each of the next Q queries, each line corresponds to one of the two types of the query. First there will be an integer denoting the type of the query, followed by the actual query. For query of type 1, there will be three space separated integers "1 p f" as defined above. For query of type 2, there will be two space separated integers "2 R ", as defined above.

-----Output-----
For each query of type 2, output two space separated integers, first digit of Chef's enjoyment in this trip followed by the value of enjoyment modulo 109 + 7.

-----Constraints-----
-  1 ≤ N, Q ≤ 105 
-  1 ≤ Fi ≤ 10^9 
-  1 ≤ f ≤ 10^9 
-  1 ≤ p ≤ N 
-  1 ≤ R ≤ N 

-----Subtasks-----
Subtask #1 (5 points) : 

-  1 ≤ N ≤ 10 
-  1 ≤ Q  ≤ 1000 
-  1 ≤ Fi ≤ 10 
-  1 ≤ f ≤ 10 

Subtask #2 (15 points) : 

-  1 ≤ N ≤ 1000 
-  1 ≤ Q  ≤ 100 
-  1 ≤ Fi ≤ 109 
-  1 ≤ f ≤ 1000 

Subtask #3 (80 points) : 

- original constraints

-----Example-----
Input:
5
1 2 3 4 5
3
2 1
1 3 10
2 2

Output:
1 120
5 50

-----Explanation-----
In the first query, Chef is going to visit cities 1, 2, 3, 4, 5 in order. At the end of the trip, his total enjoyment will be 1 * 2 * 3 * 4 * 5 = 120. First digit of enjoyment is 1 and 120 modulo 109 + 7 is 120.
In the third query, Chef is going to visit cities 1, 3, 5 in order. At the end of the trip, his total enjoyment will be 1 * 10 * 5 = 50.
"""

def calculate_enjoyment(N, friendliness, queries):
    MOD = 1000000007
    results = []
    
    for query in queries:
        if query[0] == 1:
            # Update the friendliness of the p-th city
            _, p, f = query
            friendliness[p - 1] = f
        elif query[0] == 2:
            # Calculate the enjoyment for the trip with parameter R
            _, R = query
            tot = friendliness[0]
            i = 1
            while 1 + i * R <= N:
                tot *= friendliness[i * R]
                i += 1
            
            # Find the first digit of the enjoyment
            first_digit = int(str(tot)[0])
            
            # Calculate the enjoyment modulo 10^9 + 7
            tot %= MOD
            
            # Store the result
            results.append((first_digit, tot))
    
    return results