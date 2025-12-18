"""
QUESTION:
Write a function `categorize_company` that takes an integer `industry_code` as input and returns the corresponding industry name based on the following mapping: 

1: "Other"
2: "Mining"
3: "Processing"
4: "Energy"
5: "Utilities"
6: "Construction"
7: "Retail_and_wholesale"

If the input `industry_code` is not a valid industry code, the function should return "Unknown Industry".
"""

def categorize_company(industry_code):
    industry_map = {
        1: "Other",
        2: "Mining",
        3: "Processing",
        4: "Energy",
        5: "Utilities",
        6: "Construction",
        7: "Retail_and_wholesale",
    }
    return industry_map.get(industry_code, "Unknown Industry")