"""
QUESTION:
Write a function called `calculate_total_area` that takes the number of rectangles `n` as input. Each rectangle has a length that is twice its breadth and a perimeter of 30 cm. The function should return a tuple where the first element is the total area of all the rectangles and the second element is the area of the rectangle with the largest area.
"""

def calculate_total_area(n):
    # Calculate the breadth of each rectangle
    breadth = 30 / 6  # 5 cm

    # Calculate the area of each rectangle
    area_per_rectangle = breadth * 2 * breadth  # 50 square cm

    # Calculate the total area of all rectangles
    total_area = n * area_per_rectangle

    # Since all rectangles have the same dimensions, 
    # they all have the same area, which is the largest area
    largest_area = area_per_rectangle

    return total_area, largest_area