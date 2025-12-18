"""
QUESTION:
Write a function `find_hcf_of_corrected_diff` that takes four integers as input, representing two pairs of numbers. Each pair of numbers may have one number with its digits flipped (e.g., 12 becomes 21). The function should first correct any flipped digits in the input numbers, then calculate the absolute difference between the two numbers in each pair, and finally return the highest common factor (HCF) of these two differences.
"""

def find_hcf_of_corrected_diff(a, b, c, d):
    def find_hcf(x, y):
        while(y):
            x, y = y, x % y
        return x

    def check_if_faulty(num):
        num_list = [int(i) for i in str(num)]
        if num_list[0] > num_list[1]:
            num_list[0], num_list[1] = num_list[1], num_list[0]
            return int(''.join(map(str,num_list))) 
        else:
            return num

    first_number_1 = check_if_faulty(a)
    second_number_1 = check_if_faulty(b)
    first_number_2 = check_if_faulty(c)
    second_number_2 = check_if_faulty(d)

    diff1 = abs(first_number_1-second_number_1)
    diff2 = abs(first_number_2-second_number_2)

    return find_hcf(diff1, diff2)