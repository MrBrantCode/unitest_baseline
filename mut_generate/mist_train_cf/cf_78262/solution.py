"""
QUESTION:
Write a function `honey_weight` that takes two parameters: `total_weight` (the total weight of honey in two containers) and `extracted_honey` (the amount of honey extracted from the larger container). The function should return the original weight of the honey in the larger container. After the extraction, the weight ratio of the honey in the larger container to the honey in the smaller container is 4:1.
"""

def honey_weight(total_weight, extracted_honey):
    small_container = (total_weight - extracted_honey)/5
    large_container = total_weight - extracted_honey - small_container
    large_container += extracted_honey
    return large_container