"""
QUESTION:
Implement a method `findTimeGaps` in a class that takes a list of timestamps in the format "YYYY-MM-DD HH:MM:SS" and returns a list of strings representing the time gaps between consecutive timestamps in the format "start_time - end_time". The input list is ordered and contains at least two timestamps.
"""

from typing import List
from datetime import datetime

def find_time_gaps(timestamps: List[str]) -> List[str]:
    """
    This function takes a list of timestamps in the format "YYYY-MM-DD HH:MM:SS" 
    and returns a list of strings representing the time gaps between consecutive 
    timestamps in the format "start_time - end_time".
    
    Args:
        timestamps (List[str]): A list of timestamps.
    
    Returns:
        List[str]: A list of time gaps between consecutive timestamps.
    """
    time_gaps = []
    for i in range(len(timestamps) - 1):
        start_time = datetime.strptime(timestamps[i], "%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime(timestamps[i + 1], "%Y-%m-%d %H:%M:%S")
        time_gaps.append(f"{start_time.strftime('%Y-%m-%d %H:%M:%S')} - {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    return time_gaps