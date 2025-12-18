"""
QUESTION:
Create a function called `grade` that takes an integer `score` as input. Assign a grade based on the following conditions: if the score is higher than 80 and lower than 90, check if the score is a prime number. If the score is prime, return "D", otherwise return "F".
"""

def grade(score):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if 80 < score < 90 and is_prime(score):
        return "D"
    elif 80 < score < 90:
        return "F"
    else:
        # You might want to add additional grade logic here
        return "Invalid score"