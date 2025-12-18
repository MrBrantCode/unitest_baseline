"""
QUESTION:
Implement a function `crop_classes(train_geo)` that categorizes train stations based on their geographical coordinates into three classes of service and returns a dictionary containing the count of train stations in each class. The function should categorize each station as follows:
- Class 1: If the latitude is greater than 45 and the longitude is less than -100
- Class 2: If the latitude is less than 45 and the longitude is greater than -100
- Class 3: If the latitude is greater than or equal to 45 and the longitude is greater than or equal to -100
The function should take a list of tuples representing the geographical coordinates of train stations and return a dictionary where the keys are the class numbers (1, 2, 3) and the values are the counts of stations in each class.
"""

def categorize_train_stations(train_geo):
    class_counts = {1: 0, 2: 0, 3: 0}
    
    for station in train_geo:
        latitude, longitude = station
        if latitude > 45 and longitude < -100:
            class_counts[1] += 1
        elif latitude < 45 and longitude > -100:
            class_counts[2] += 1
        else:
            class_counts[3] += 1
    
    return class_counts