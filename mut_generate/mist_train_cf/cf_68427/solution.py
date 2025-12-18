"""
QUESTION:
Design a function named `cpu_read_data` that reads data from a memory address, utilizing cache memory and main memory. The function should first check the cache memory for the requested data, and if not found (cache miss), it should retrieve the data from the main memory and store it in the cache for future access. If the data is not found in the main memory, it should be retrieved from the storage device. The function should return the requested data. Assume the existence of `cache`, `main_memory`, and `storage` objects with `get` and `store` methods. The function should handle cases where the data is not found in any of the memory levels.
"""

def cpu_read_data(memory_address, cache, main_memory, storage):
    """
    Reads data from a memory address, utilizing cache memory and main memory.

    Args:
    memory_address (str): The memory address to read from.
    cache (object): The cache memory object with 'get' and 'store' methods.
    main_memory (object): The main memory object with 'get' and 'store' methods.
    storage (object): The storage device object with 'get' and 'store' methods.

    Returns:
    data (any): The data read from the memory address.

    """
    data = cache.get(memory_address)
    if data is None:
        data = main_memory.get(memory_address)
        if data is not None:
            cache.store(memory_address, data)
        else:
            data = storage.get(memory_address)
            if data is not None:
                main_memory.store(memory_address, data)
                cache.store(memory_address, data)
    return data