"""
QUESTION:
Write a Python function named `sum_and_avg` that takes three numbers as arguments, calculates and prints their sum and average (rounded to two decimal places), and returns the sum and average. Additionally, create a table that displays the factors of each number up to 20.
"""

def sum_and_avg(num1, num2, num3):
    total = num1 + num2 + num3
    avg = round(total / 3, 2)
    print("Sum:", total)
    print("Average:", avg)

    print("\nFactors of each number up to 20:")
    for num in [num1, num2, num3]:
        print("\nFactors of", num)
        for i in range(1, 21):
            if num % i == 0:
                print(i)
    return total, avg