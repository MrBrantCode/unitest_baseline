"""
QUESTION:
Write a function `calculate_average_yield(crop_data)` that takes a list of tuples representing crops as input. Each tuple contains information about the crop, including its type, ID, yield, and acreage. The function should return a dictionary where the keys are unique crop types and the values are the average yield for each crop type. The average yield is calculated by dividing the total yield by the acreage for each crop type.
"""

def calculate_average_yield(crop_data):
    crop_yield = {}
    crop_count = {}
    
    for crop in crop_data:
        crop_type = crop[0]
        total_yield = crop[2]
        acreage = crop[3]
        
        if crop_type in crop_yield:
            crop_yield[crop_type] += total_yield * acreage
            crop_count[crop_type] += acreage
        else:
            crop_yield[crop_type] = total_yield * acreage
            crop_count[crop_type] = acreage
    
    average_yield = {crop: crop_yield[crop] / crop_count[crop] for crop in crop_yield}
    return average_yield