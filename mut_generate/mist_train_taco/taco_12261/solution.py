"""
QUESTION:
IOI Real Estate rents condominiums. The apartment room handled by this company is 1LDK, and the area is 2xy + x + y as shown in the figure below. However, x and y are positive integers.


Figure_Madori


In the IOI real estate catalog, the areas of condominiums are listed in ascending order (in ascending order), but it was found that some mistakes (those with an impossible area) were mixed in this.

The catalog (input file) has N + 1 lines, the number of rooms is written in the first line, and the area is written in ascending order, one room per line in the following N lines. However, the number of rooms is 100,000 or less, and the area is (2 to the 31st power) -1 = 2,147,483,647 or less. Up to 3 of the 5 input data have 1000 rooms or less and an area of ​​30000 or less.

Output the wrong number of lines (the number of impossible rooms).

In the output file, also include a line feed code on the last line of the output.





Examples

Input

10
4
7
9
10
12
13
16
17
19
20


Output

2


Input

None


Output

None
"""

def count_impossible_rooms(catalog):
    """
    Counts the number of impossible rooms in the catalog based on the formula 2xy + x + y.

    Parameters:
    catalog (list of int): A list of integers representing the areas of the condominiums in ascending order.

    Returns:
    int: The number of impossible rooms.
    """
    def is_possible_area(a):
        """
        Checks if the given area 'a' can be represented by the formula 2xy + x + y.

        Parameters:
        a (int): The area to be checked.

        Returns:
        int: 1 if the area is possible, 0 otherwise.
        """
        for i in range(2, int(a ** (1 / 2)) + 1):
            if a % i == 0:
                return 1
        return 0

    count = 0
    for area in catalog:
        if is_possible_area(2 * area + 1) == 0:
            count += 1
    return count