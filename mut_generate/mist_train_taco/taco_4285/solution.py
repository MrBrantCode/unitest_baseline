"""
QUESTION:
Kuldeep and his girlfriend Cristie are both huge math nerds, so for their first anniversary he decides to take her out on a romantic getaway to Mathland, the city of mathematics and love. 

Now Kuldeep's arch-nemesis Rishabh, jealous of the perfect relationship between Kuldeep and Cristie, kidnaps Kuldeep's girl and imprisons her at the top floor of his dungeon.

Surprisingly the dungeon is in an apartment complex of n floors, numbered 1 to n, and being short on cash Rishabh can only lease some floors (continious) for his dungeon from floor a to floor b (inclusive).

Also to make sure so that Kulddep cannot come and rescue his girlfriend, Rishabh places guards on some of the floors he has leased.

Being a bit eccentric, he only places guards on those floors from a to b (inclusive), where the floor number has highest number of divisors.

Kuldeep apart from being a math genius is extremely proficient in the art of Wu Shu, a type of Chinese martial art, so it's easy for him to defeat the guards but he still takes 1 unit of health damage per guarded floor and Kuldeep dies if his health ever reaches 0 or less.

Your task is to help Kuldeep find the minimum amount of health units he needs to reach Cristie.

Input : 

first line contain number of test cases T , next T line contains two numbers a and b.

Output :

Output minimum amount of health units he needs to reach Cristie.

Constraints:
1 ≤ T ≤ 100
1 ≤ n(number of floors) ≤ 10^8
0 ≤ b-a ≤ 10^4

SAMPLE INPUT
2
2 9
1 10SAMPLE OUTPUT
3
4Explanation

In first test case with a=2 and b=9, 6 and 8 are the floors with numbers which have highest number of divisors.So guards are placed at 2 floors only, therefore Kuldeep needs minimum 3 units of health to reach Cristie.

Similarly for second test case with a=1 and b=10, floor numbers with highest number of divisors are 6,8 and 10, so minimum health units required is 4.
"""

def calculate_minimum_health(T, test_cases):
    def primes_sieve1(limit):
        limitn = limit + 1
        primes = dict()
        for i in range(2, limitn):
            primes[i] = True

        for i in primes:
            factors = list(range(i, limitn, i))
            for f in factors[1:]:
                primes[f] = False
        return [i for i in primes if primes[i] == True]

    primes = primes_sieve1(130)

    def smartDivisorGenerator(n):
        limit = 1
        for val in primes:
            counter = 1
            while True:
                if n % val == 0:
                    counter += 1
                    n = n / val
                else:
                    break
            limit = limit * counter
        return limit

    results = []
    for case in test_cases:
        a, b = case
        max_divisors = 0
        guarded_floors = 0
        for val in range(a, b + 1):
            div = smartDivisorGenerator(val)
            if div > max_divisors:
                guarded_floors = 0
                max_divisors = div
                guarded_floors += 1
            elif div == max_divisors:
                guarded_floors += 1
        results.append(guarded_floors + 1)
    
    return results