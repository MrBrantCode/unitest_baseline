"""
QUESTION:
Write a function `magicTransform` that takes a non-empty dictionary where keys are real numbers and values represent lists of integers. The function should add the elements in the lists that are at fraction keys and divisible by 4, then multiply the sum by the first 3 prime numbers in each list that are divisible by 3. Return the total sum calculated from all fraction keys in the dictionary.
"""

def magicTransform(my_dict):
    total_sum = 0
    for key in my_dict:
        if key % 1 != 0: 
            num_list = my_dict[key]
            sum_nums = sum(i for i in num_list if i % 4 == 0)

            primes_div_3 = [i for i in num_list if i > 1 if all(i % d for d in range(2, int(i**0.5)+1)) and i%3 == 0] 
            if len(primes_div_3) < 3:
                prod_primes = 1 if not primes_div_3 else eval('*'.join(str(i) for i in primes_div_3))
            else:
                prod_primes = eval('*'.join(str(i) for i in primes_div_3[:3]))

            total_sum += sum_nums * prod_primes
    return total_sum