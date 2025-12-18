"""
QUESTION:
Create a function called 'iterate_and_classify' that takes a list of integers as input. The function should iterate over the list, printing the index and value of each element. For each element, it should also print whether the number is even or odd. Additionally, the function should store the even numbers in a separate list and return it.
"""

def iterate_and_classify(collection):
    even_elements = []
    
    for index, element in enumerate(collection):
        print("Index:", index, "Element:", element)
        
        if element % 2 == 0:
            print("Even")
            even_elements.append(element)
        else:
            print("Odd")
            
    return even_elements