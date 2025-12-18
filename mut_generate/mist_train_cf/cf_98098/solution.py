"""
QUESTION:
Implement a recursive function called `add_element_to_list` that takes two parameters, an element and a list, and adds the element to the list without duplicates. Implement another recursive function called `remove_element_from_list` that takes two parameters, an element and a list, and removes the element from the list. Implement two more recursive functions, `add_range_to_list` and `remove_range_from_list`, that take a range and a list of ranges and add or remove the range from the list while handling overlapping ranges. The list of ranges should be sorted in ascending order of the start values of the ranges, and the ranges should not overlap or touch each other.
"""

def add_element_to_list(element, my_list):
    if not my_list:
        return [element]
    else:
        if my_list[0] == element:
            return my_list
        else:
            return [my_list[0]] + add_element_to_list(element, my_list[1:])

def remove_element_from_list(element, my_list):
    if not my_list:
        return []
    else:
        if my_list[0] == element:
            return my_list[1:]
        else:
            return [my_list[0]] + remove_element_from_list(element, my_list[1:])

def add_range_to_list(start, end, my_list):
    if not my_list:
        return [(start, end)]
    else:
        if end < my_list[0][0]:
            return [(start, end)] + my_list
        elif start > my_list[-1][1]:
            return my_list + [(start, end)]
        else:
            i = 0
            while i < len(my_list):
                if end < my_list[i][0]:
                    return my_list[:i] + [(start, end)] + my_list[i:]
                elif start > my_list[i][1]:
                    i += 1
                else:
                    return add_range_to_list(min(start, my_list[i][0]), max(end, my_list[i][1]), my_list[:i] + my_list[i+1:])

def remove_range_from_list(start, end, my_list):
    if not my_list:
        return []
    else:
        if end < my_list[0][0]:
            return my_list
        elif start > my_list[-1][1]:
            return my_list
        else:
            i = 0
            while i < len(my_list):
                if end < my_list[i][0]:
                    return my_list
                elif start > my_list[i][1]:
                    i += 1
                else:
                    if start <= my_list[i][0] and end >= my_list[i][1]:
                        return remove_range_from_list(start, end, my_list[:i] + my_list[i+1:])
                    elif start <= my_list[i][0] and end < my_list[i][1]:
                        return [(end+1, my_list[i][1])] + my_list[i+1:]
                    elif start > my_list[i][0] and end >= my_list[i][1]:
                        return my_list[:i] + [(my_list[i][0], start-1)] + remove_range_from_list(start, end, my_list[i+1:])
                    else:
                        return my_list[:i] + [(my_list[i][0], start-1), (end+1, my_list[i][1])] + my_list[i+1:]