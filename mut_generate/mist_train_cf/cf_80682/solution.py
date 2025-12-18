"""
QUESTION:
Write a function `unordered_sort` that takes a list of positive integers and a string `order` as input, where `order` is either "asc" for ascending or "desc" for descending. The function should return the list sorted in the specified order with all duplicates removed, without using the built-in `sorted()` function, `.sort()` method, or `set` data type in Python.
"""

def unordered_sort(inp_list, order="asc"):
    
    ## Sorting Algorithm
    # start iterating each element
    for i in range(0,len(inp_list)):
        # compare with all the elements after i 
        for j in range(i+1,len(inp_list)):
            if order=="asc":
                # if the next element is smaller than current element, swap
                if inp_list[i] > inp_list[j]:
                    temp = inp_list[i]
                    inp_list[i] = inp_list[j]
                    inp_list[j] = temp
            elif order=="desc":
                # if the next element is bigger than current element, swap
                if inp_list[i] < inp_list[j]:
                    temp = inp_list[i]
                    inp_list[i] = inp_list[j]
                    inp_list[j] = temp

    ## Removing Duplicates
    # creating an empty list
    final_list = []
    for num in inp_list:
        # checking for duplicates
        if num not in final_list:
            final_list.append(num)
            
    return final_list