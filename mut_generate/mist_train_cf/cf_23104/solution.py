"""
QUESTION:
Write a function `filter_numbers` that takes a list of integers as input. Filter out numbers that are divisible by both 3 and 5 but not by 2, and store them in a new list. Print the sum of the filtered numbers. If the input list is empty, print "No numbers to filter." If the input list contains non-integer values, skip those values. Also, check if each filtered number is prime and print a corresponding message. If no numbers are filtered, print "No numbers filtered."
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_numbers(numbers):
    if not numbers:
        print("No numbers to filter.")
        return

    filtered_numbers = []
    for num in numbers:
        if isinstance(num, int):
            if num % 3 == 0 and num % 5 == 0 and num % 2 != 0:
                filtered_numbers.append(num)
    if not filtered_numbers:
        print("No numbers filtered.")
        return

    print("Filtered numbers:", filtered_numbers)
    print("Sum of filtered numbers:", sum(filtered_numbers))
    for num in filtered_numbers:
        if is_prime(num):
            print(num, "is a prime number.")
        else:
            print(num, "is not a prime number.")