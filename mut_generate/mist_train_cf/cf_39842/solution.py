"""
QUESTION:
Implement the `calculate_data_source_size` method within the `HDF5Processor` class that takes the `datasource_name` as input and returns the total size of the specified data source. The total size is calculated based on the data type and number of channels defined in the `data_types` and `num_channels` class dictionaries, respectively. If the `datasource_name` is not found in these dictionaries, the method should return 0.
"""

import numpy as np

def calculate_data_source_size(datasource_name, data_types, num_channels):
    if datasource_name in data_types and datasource_name in num_channels:
        data_type_size = np.dtype(data_types[datasource_name]).itemsize
        total_size = data_type_size * num_channels[datasource_name]
        return total_size
    else:
        return 0