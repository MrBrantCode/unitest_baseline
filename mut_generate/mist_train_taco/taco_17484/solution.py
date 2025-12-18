"""
QUESTION:
A certain business maintains a list of all its customers' names. The list is arranged in order of importance, with the last customer in the list being the most important. Now, he want to create a new list sorted alphabetically according to customers' last names, but among customers with the same last name he want the more important ones to appear earlier in the new list. Alphabetical order (and equality of last names) should not be case sensitive.

Input:-
First line contains no. of test cases and first line of each test case contains n i.e. no. of elements and next n lines contains contains a name.

Output:- Print the new list with each element in a new line.

SAMPLE INPUT
2
5
Tom Jones
ADAMS
BOB ADAMS
Tom Jones
STEVE jONeS
3
Trudy
Trudy
TRUDY

SAMPLE OUTPUT
BOB ADAMS
ADAMS
STEVE jONeS
Tom Jones
Tom Jones
TRUDY
Trudy
Trudy
"""

def sort_customers_by_last_name(test_cases):
    sorted_lists = []
    
    for case in test_cases:
        dic = {}
        last_names = []
        
        for name in case:
            parts = name.split()
            last_name = parts[-1].lower()
            
            if last_name not in last_names:
                last_names.append(last_name)
            
            if last_name in dic:
                dic[last_name].append(parts)
            else:
                dic[last_name] = [parts]
        
        last_names.sort()
        sorted_case = []
        
        for last_name in last_names:
            for name_parts in reversed(dic[last_name]):
                sorted_case.append(' '.join(name_parts))
        
        sorted_lists.append(sorted_case)
    
    return sorted_lists