"""
QUESTION:
Implement a function named custom_divisible that takes four positive integers x, y, z, and k as inputs. The function should find and return the kth smallest even prime number within the range [x, y] that can be proportionally divided by z. If there are fewer than k such numbers within this range or the numeric range is incorrect (x > y or k <= 0), the function should return -1. The function needs to handle large inputs efficiently, with x, y, z up to 1,000,000 and k up to 1000, without using any external libraries.
"""

def custom_divisible(x, y, z, k):
    if x>y or k<=0:
        return -1
    else:
        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        even_nums_divisible_by_z = [i for i in range(y, x - 1, -1) if i % z == 0 and i % 2 == 0 and is_prime(i)]
        if len(even_nums_divisible_by_z) < k:
            return -1
        else:
            return even_nums_divisible_by_z[k - 1]