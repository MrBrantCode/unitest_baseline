"""
QUESTION:
Create a function called `triangular_num` that takes an integer `n` as input and returns the total sum of a 3D pyramid of triangular numbers, where the pyramid is constructed by arranging triangular numbers up to the `n`th term. The function should not use any built-in functions to calculate the triangular numbers. For each level of the pyramid, calculate the cumulative sum and print it. The function should return the total sum of all levels.
"""

def triangular_num(n):
    total_sum = 0
    curr_level_sum = 0
    num = 0
    level = 0

    while n > 0:
        level += 1
        curr_level_sum = 0

        for i in range(level):
            if n > 0:
                num +=1
                curr_level_sum += num
                n -= 1
            else:
                break

        print("Level", level, "Sum:", curr_level_sum)
        total_sum += curr_level_sum

    return total_sum