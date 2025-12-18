"""
QUESTION:
Implement a function `sort_list(mylist, sort_order, sort_by)` that sorts a given list of numbers based on the specified order and criteria. The `sort_order` parameter can be either "asc" for ascending or "desc" for descending. The `sort_by` parameter can be "all" to sort the entire list, "even" to sort only even numbers, or "odd" to sort only odd numbers. The function should not use any built-in sorting functions or libraries.
"""

def sort_list(mylist, sort_order, sort_by):
    def bubble_sort(mylist):
        for passnum in range(len(mylist) - 1, 0, -1):
            for i in range(passnum):
                if mylist[i] > mylist[i + 1]:
                    temp = mylist[i]
                    mylist[i] = mylist[i + 1]
                    mylist[i + 1] = temp
        return mylist

    if sort_by == "even":
        even_list = [i for i in mylist if i % 2 == 0]
        odd_list = [i for i in mylist if i % 2 != 0]    
        sorted_even_list = bubble_sort(even_list)
        if sort_order == "desc":
            sorted_even_list.reverse()
        return sorted_even_list + odd_list

    elif sort_by == "odd":
        odd_list = [i for i in mylist if i % 2 != 0]
        even_list = [i for i in mylist if i % 2 == 0]
        sorted_odd_list = bubble_sort(odd_list)
        if sort_order == "desc":
            sorted_odd_list.reverse()
        return even_list + sorted_odd_list
    
    # sort all 
    else:
        sorted_list = bubble_sort(mylist)
        if sort_order == "desc":
            sorted_list.reverse()
        return sorted_list