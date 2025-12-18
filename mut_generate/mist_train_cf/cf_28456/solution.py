"""
QUESTION:
Implement a `PrecisionCalculator` class with the following methods:
- `add_page_precision(tolerance_level, line_number, precision_value)`: appends the precision value to the page-wise precision list for the specified tolerance level and line number.
- `calculate_per_line_precision()`: calculates the precision per line for each tolerance level and returns a dictionary where the keys are tolerance levels and the values are lists of precision values per line.
- `calculate_per_tol_overall_precision()`: calculates the overall page-wise precision for each tolerance level and returns a dictionary where the keys are tolerance levels and the values are the overall precision values.

No additional information is provided about the input or output data types, so it is assumed that `tolerance_level` and `line_number` are integers, and `precision_value` is a number. The class should be able to handle an arbitrary number of tolerance levels and lines.
"""

import numpy as np

def PrecisionCalculator(tolerance_level, line_number, precision_value):
    class PrecisionCalculator:
        def __init__(self):
            self.page_wise_per_dist_tol_tick_per_line_precision = []

        def add_page_precision(self, tolerance_level, line_number, precision_value):
            # Ensure that the page-wise precision list is initialized for the tolerance level
            while len(self.page_wise_per_dist_tol_tick_per_line_precision) <= tolerance_level:
                self.page_wise_per_dist_tol_tick_per_line_precision.append([])

            # Append the precision value to the page-wise precision list for the specified tolerance level and line number
            self.page_wise_per_dist_tol_tick_per_line_precision[tolerance_level].append((line_number, precision_value))

        def calculate_per_line_precision(self):
            per_line_precision = {}
            for tolerance_level, precision_list in enumerate(self.page_wise_per_dist_tol_tick_per_line_precision):
                per_line_precision[tolerance_level] = [precision for _, precision in precision_list]
            return per_line_precision

        def calculate_per_tol_overall_precision(self):
            per_tol_overall_precision = {}
            for tolerance_level, precision_list in enumerate(self.page_wise_per_dist_tol_tick_per_line_precision):
                overall_precision = np.sum([precision for _, precision in precision_list])
                per_tol_overall_precision[tolerance_level] = overall_precision
            return per_tol_overall_precision

    return PrecisionCalculator()