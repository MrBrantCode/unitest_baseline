"""
QUESTION:
Create a function `my_sort` that takes a list of tuples as an argument. Each tuple contains two integers and a string. The function should sort the list in ascending order of the first integer, then in descending order of the second integer, and finally in descending order of the string length. The function should not use Python's built-in sort function or any similar library functions. Instead, it should implement a custom sorting algorithm.
"""

def my_sort(my_list):
    n = len(my_list)

    for i in range(n):
        for j in range(0, n-i-1):
            if my_list[j][0] > my_list[j+1][0] or \
              (my_list[j][0] == my_list[j+1][0] and my_list[j][1] < my_list[j+1][1]) or \
              (my_list[j][0] == my_list[j+1][0] and my_list[j][1] == my_list[j+1][1] and len(my_list[j][2]) < len(my_list[j+1][2])):
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list