"""
QUESTION:
Sid is a superior salesperson. So he gets a task from his boss. The task is that he will be given some number of products say k (All the products are same) and he has to travel N cities [1...N] to sell them. The main objective of the task is that he has to try to sell the product at higher price than previous city. For example if he sells a product at 100 Rs in one city then he has to try to sell the next product greater than 100 Rs in the next city and so on.
He travels all the cities and write down all the selling amounts. Now He wants to calculate maximum number of cities in which he could follow this increasing trend. And the maximum total prime money he could make in those cities. Help him in  finding this.
Note : Number of products will always be equal to number of cities. 
 
Example 1:
Input:
N = 9
A[] = {4, 2, 3, 5, 1, 6, 7, 8, 9}
Output:
5 7
Explanation:
5 cities are maximum number of 
cities in which the trend 
followed, And  amount in those 
cities were 1, 6, 7, 8, 9. 
Out of  these  amounts only 
7 is prime money.
 
Example 2:
Input:
N = 10
A[] = {2, 3, 5, 7, 4, 1, 6, 5, 4, 8}
Output:
4 17
Explanation:
4 cities are maximum number of 
cities in which the trend 
followed, And  amount in those 
cities were 2, 3, 5, 7. 
Out of  these amounts, maximum
total prime money is 2+3+5+7=17.
 
Example 3:
Input:
N = 5
A[] = {2, 2, 2, 2, 2}
Output:
1 2
Explanation:
He was successful in one city 
only, And maximum total prime 
money is 2.
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function primeMoney() which takes the array A[] and its size N as inputs and returns the maximum number of cities and maximum total prime money as a pair. 
Expected Time Complexity: O(N. sqrt(N))
Expected Auxiliary Space: O(N)
 
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ A[i] ≤ 10^{5 }
"""

def calculate_max_increasing_trend_and_prime_money(A, N):
    # Helper function to check if a number is prime
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
    
    # Generate all prime numbers up to the maximum value in A
    maxi = max(A)
    primes = set()
    for i in range(2, maxi + 1):
        if is_prime(i):
            primes.add(i)
    
    count = 0
    summa = 0
    last = 0
    temp_count = 0
    temp_summa = 0
    
    for item in A:
        if item > last:
            temp_count += 1
            if item in primes:
                temp_summa += item
        else:
            if temp_count > count:
                count = temp_count
                summa = temp_summa
            elif temp_count == count:
                summa = max(summa, temp_summa)
            temp_count = 1
            if item in primes:
                temp_summa = item
            else:
                temp_summa = 0
        last = item
    
    if temp_count > count:
        count = temp_count
        summa = temp_summa
    elif temp_count == count:
        summa = max(summa, temp_summa)
    
    return count, summa