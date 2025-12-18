"""
QUESTION:
Create a function `get_dir_files_by_date` that takes a directory path as input and returns a dictionary mapping each file path in the directory to its creation date. The files should be sorted in descending order by creation date. The function should handle potential errors that may occur during the file retrieval process, such as the directory not existing or lack of permission to access it.
"""

from datetime import datetime
from typing import Dict
from pathlib import Path

def get_dir_files_by_date(path: Path) -> Dict[Path, datetime]:
    """Get all files in the specified directory, sorted by creation date (desc),
    along with the parsed datetime.
    """
    try:
        files = list(path.iterdir())
        file_dates = {file: file.stat().st_ctime for file in files if file.is_file()}
        sorted_files = sorted(file_dates.items(), key=lambda x: x[1], reverse=True)
        return {file: datetime.fromtimestamp(timestamp) for file, timestamp in sorted_files}
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while accessing directory: {e}")
        return {}