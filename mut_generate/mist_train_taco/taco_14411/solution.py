"""
QUESTION:
A list of names is taken as input, in which a particular name can occur multiple times. You need to arrange these names as they will appear in the dictionary and also print the number of times the arranged names appear in the list taken as input.

Input:

The first line of input contains an integer, t, which denotes the number of names that will follow. 

Then, t lines follow, each containing a name, in the form of a character string S.

Output:

The output contains the names as they would appear in the dictionary, followed by the frequency of that name in the list. 

Constraints:

1 ≤ t ≤ 100000
1 ≤ |S| ≤30
S contains only lower case characters.

SAMPLE INPUT
3
ritesh
sahil
ritesh

SAMPLE OUTPUT
ritesh 2
sahil 1

Explanation

Test Case #1:

As the name starts from 'r' comes first then 's' in dictionary and in this case the 'ritesh' name is given 2 times and 'sahil' is given only once so their frequency is coming and remove the duplicate rows.
"""

def count_and_sort_names(names):
    # Step 1: Sort the names in dictionary order
    sorted_names = sorted(names)
    
    # Step 2: Initialize the result list
    sorted_names_with_counts = []
    
    # Step 3: Iterate through the sorted names and count frequencies
    i = 0
    while i < len(sorted_names):
        name = sorted_names[i]
        count = 1
        while i + 1 < len(sorted_names) and sorted_names[i + 1] == name:
            count += 1
            i += 1
        sorted_names_with_counts.append((name, count))
        i += 1
    
    return sorted_names_with_counts