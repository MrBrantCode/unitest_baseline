"""
QUESTION:
Create a function `calculateHeapSize` that takes the total available memory in gigabytes as input and returns the recommended heap size in gigabytes. The function should follow these guidelines:
- If available memory is less than or equal to 2GB, return 0.5GB.
- If available memory is between 2GB and 4GB, return 1GB.
- If available memory is between 4GB and 8GB, return 2GB.
- If available memory is greater than 8GB, return half of the available memory, rounded down to the nearest whole number.
"""

def calculateHeapSize(available_memory_gb):
    if available_memory_gb <= 2:
        return 0.5  
    elif available_memory_gb <= 4:
        return 1  
    elif available_memory_gb <= 8:
        return 2  
    else:
        return available_memory_gb // 2 