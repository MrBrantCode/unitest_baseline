"""
QUESTION:
Write a function `alternate_fibo_and_sum(min_range, max_range)` that prints every alternate Fibonacci sequence number within a given range (`min_range` to `max_range`) and also prints the sum of these numbers.
"""

def alternate_fibo_and_sum(min_range, max_range):
    def fibo(n):
        fib_list = [0, 1]
        for i in range(2, n):
            fib_list.append(fib_list[i-1] + fib_list[i-2])
        return fib_list

    fib_nums = fibo(max_range)
    alternate_fib_nums = [num for i, num in enumerate(fib_nums) if num >= min_range and i % 2 != 0]
    print("The alternate Fibonacci sequence numbers between {0} and {1} are:".format(min_range, max_range))
    for i in alternate_fib_nums:
        print(i)
    print("The sum of these numbers is:", sum(alternate_fib_nums))