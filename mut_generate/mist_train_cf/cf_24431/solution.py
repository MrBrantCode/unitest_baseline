"""
QUESTION:
Design a function called `access_data` that can retrieve data from multiple data sources. The function should be able to handle different types of data sources without modification, allowing for easy addition of new data sources in the future.
"""

def access_data(data_source):
    """
    A function used to retrieve data from multiple data sources.

    Args:
    ----
    data_source : object
        An object representing the data source. The object should have a read method.

    Returns:
    -------
    data : 
        The data retrieved from the data source.
    """
    return data_source.read()