"""
QUESTION:
Chinna is preparing for an online entrance examination. The performance in the examination is measured on a rating scale of 1 to 10^6. Recently, Chinna came across an advertisement of an institution which guarantees an increase of 'd' in the rating for an examination for an hour of coaching. Chinna wants to excel the performance compared to previous examination each time he takes up a test. Now, Chinna wants to spend minimum time on coaching and asks Chinnu for help to figure out the total time he needs to put on coaching.

Input  Format:

n : Number of examinations Chinna is going to take up

d : Increase in the rating that the institution has guaranteed

ai : Rating that Chinna is expected to achieve in the i th examination

Output Fomat:

Single integer containing the number of hours of coaching needed

Constraints:

1 ≤ n ≤ 2000

1 ≤ d,a[i] ≤ 10^6

SAMPLE INPUT
5
82
61 28 956 75 542

SAMPLE OUTPUT
18

Explanation

There is nothing to bother about the 1st exam. But Chinna needs to improve in the second test and can make a progress of 110 with 1 hour coaching. Performance has increased for 3rd test so no coaching required. For 4th one, he should make a progress of 977 with 11 hours of coaching. For last one, he needs 6 hours of coaching to make the progress to 1034.
So, in total, 18 hours are required.
"""

def calculate_minimum_coaching_time(n, d, ratings):
    time = 0
    prev_rating = ratings[0]
    
    for i in range(1, n):
        current_rating = ratings[i]
        if current_rating <= prev_rating:
            temp = (prev_rating - current_rating) / d
            values = [temp, temp + 1]
            index = 0
            while current_rating <= prev_rating:
                current_rating += values[index] * d
                if current_rating <= prev_rating:
                    current_rating -= values[index] * d
                else:
                    time += values[index]
                index += 1
        prev_rating = current_rating
    
    return time