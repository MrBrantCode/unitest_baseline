"""
QUESTION:
Implement a function `calculate_data_range` that calculates the range of data being processed for each block. The function should take five parameters: the starting index of the data being processed for the current block (`N_st`), the total number of data points to be processed (`N_cut`), the size of each data block (`Nt_block`), the number of blocks into which the data is divided (`N_div`), and the increment of data for each block (`Nt_inc`). The function should return a list of strings, where each string represents the range of data being processed for a specific block in the format "from x to y".
"""

def calculate_data_range(N_st, N_cut, Nt_block, N_div, Nt_inc):
    data_ranges = []
    for i in range(N_div):
        start_index = N_st + (i * Nt_block)
        end_index = min(start_index + Nt_block, N_cut)
        data_ranges.append('from %d to %d' % (start_index, end_index))
    return data_ranges