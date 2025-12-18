"""
QUESTION:
The function `validation_settings` should take in five parameters: `dataset_size`, `batch_size`, `val_size`, `val_interval`, and `keep_best_model`. It should return a tuple containing the calculated validation size and interval based on the following rules: 
- If `val_size` is provided, use it as the validation size; otherwise, set it to 0.2 times the dataset size.
- If `val_interval` is provided, use it as the validation interval; otherwise, set it to 0.1 times the total number of batches in one epoch.
The `keep_best_model` parameter is not used in the calculation and can be any boolean value. The `val_size` and `val_interval` default to 0 and None respectively if not provided.
"""

from typing import Tuple, Optional

def entrance(dataset_size: int, batch_size: int, val_size: int = 0, val_interval: Optional[int] = None, keep_best_model: bool = False) -> Tuple[int, Optional[int]]:
    if val_size == 0:
        val_size = int(0.2 * dataset_size)
    
    if val_interval is None:
        val_interval = int(0.1 * (dataset_size / batch_size))
    
    return val_size, val_interval