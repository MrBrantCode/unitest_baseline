"""
QUESTION:
Design a function `compute_mean_price` that takes a dataset as input and returns the mean of the "Price" column for the rows where the "Quantity" values fall within the range of the minimum and maximum values of the "Quantity" column (inclusive).
"""

def compute_mean_price(dataset):
    min_quantity = min(dataset["Quantity"])
    max_quantity = max(dataset["Quantity"])
    filtered_data = dataset[(dataset["Quantity"] >= min_quantity) & (dataset["Quantity"] <= max_quantity)]
    mean_price = filtered_data["Price"].mean()
    return mean_price