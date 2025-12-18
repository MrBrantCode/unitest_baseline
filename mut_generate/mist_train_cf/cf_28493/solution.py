"""
QUESTION:
Implement a method `_filter_stat` that takes a list of system statistics and an optional boolean parameter `avg` (default is False). The method should filter the statistics based on the presence of "cpu" in each line. If `avg` is False, return the filtered statistics. If `avg` is True, calculate the average of the CPU statistics from the first line and return it as a formatted string. If no CPU statistics are found, return a message indicating this.
"""

def filter_stat(stat, avg=False):
    """
    Filter system statistics based on the presence of 'cpu' in each line.
    
    Args:
    stat (list): A list of system statistics.
    avg (bool): Optional boolean parameter to calculate average CPU usage. Defaults to False.
    
    Returns:
    list or str: Filtered statistics if avg is False, otherwise the average CPU usage as a formatted string.
    """
    
    if not avg:
        # Filter the statistics based on the presence of "cpu" in each line
        filtered_stat = [line for line in stat if "cpu" in line]
        return filtered_stat
    else:
        # Filter the CPU statistics
        cpu_stats = [line for line in stat if "cpu" in line]
        
        if not cpu_stats:
            # Return a message if no CPU statistics are found
            return "No CPU statistics found"
        else:
            # Extract CPU values from the first line
            cpu_values = [int(val) for val in cpu_stats[0].split()[1:]]
            
            # Calculate the average CPU usage
            avg_cpu = sum(cpu_values) / len(cpu_values)
            
            # Return the average CPU usage as a formatted string
            return f"Average CPU usage: {avg_cpu:.2f}"