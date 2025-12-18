"""
QUESTION:
Implement a function `simulate_interrupt_controller` that takes in two initial 32-bit register states (`initial_clear_register` and `initial_enable_register`) and a list of interrupt numbers (`interrupt_numbers`) in the range of 0 to 31 (inclusive). For each interrupt number, set the corresponding bit in both `initial_clear_register` and `initial_enable_register` to 1. Return the final states of the two registers after processing all interrupt numbers.
"""

from typing import List, Tuple

def simulate_interrupt_controller(initial_clear_register: int, initial_enable_register: int, interrupt_numbers: List[int]) -> Tuple[int, int]:
    clear_register = initial_clear_register
    enable_register = initial_enable_register

    for interrupt_number in interrupt_numbers:
        # Set the corresponding bit in the clear register
        clear_register |= 1 << interrupt_number
        # Set the corresponding bit in the enable register
        enable_register |= 1 << interrupt_number

    return clear_register, enable_register