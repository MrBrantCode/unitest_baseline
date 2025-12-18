"""
QUESTION:
Write a function `memory_allocator_tests` that unit tests a memory allocator function by checking its behavior under different scenarios, including successful and failed allocations, memory reuse, and specific allocation strategies. The function should take a memory allocator function as input and return a boolean indicating whether all tests pass. Assume the memory allocator function has `malloc`, `realloc`, and `free` methods.
"""

def memory_allocator_tests(allocator):
    # Request small, medium, and large blocks of memory
    small_block = allocator.malloc(10)
    assert small_block is not None
    medium_block = allocator.malloc(100)
    assert medium_block is not None
    large_block = allocator.malloc(1000)
    assert large_block is not None

    # Request a block of memory that is larger than what's available
    too_large_block = allocator.malloc(allocator.total_memory + 1)
    assert too_large_block is None

    # Free blocks of memory and make new allocations
    allocator.free(small_block)
    reused_block = allocator.malloc(10)
    assert reused_block is not None

    # Allocate various blocks of memory, free some of them and then make new allocations
    blocks = [allocator.malloc(10) for _ in range(10)]
    for block in blocks[::2]:
        allocator.free(block)
    new_blocks = [allocator.malloc(10) for _ in range(5)]
    for new_block in new_blocks:
        assert new_block is not None

    # Allocate and free blocks of memory under high load
    for _ in range(100):
        block = allocator.malloc(10)
        assert block is not None
        allocator.free(block)

    return True