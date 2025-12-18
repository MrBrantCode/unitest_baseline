"""
QUESTION:
Implement a method `perform_operation` in the `Pkhbt` class that takes no parameters and returns the result of the operation `(m << shift_t) ^ (d >> shift_n)`. The class `Pkhbt` has an initializer method `__init__` that takes in six parameters: `tb_form`, `m`, `d`, `n`, `shift_t`, and `shift_n`, which are used to initialize the instance variables. The class inherits from `AbstractOpcode`.
"""

def perform_operation(tb_form, m, d, n, shift_t, shift_n):
    return (m << shift_t) ^ (d >> shift_n)