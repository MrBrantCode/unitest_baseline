"""
QUESTION:
Implement a class `FrequencyScale` with methods to calculate frequency range, cents per value, and convert frequencies to cents. The class should have an initializer method `__init__(self, f_min, f_max, v_min, v_max)` to set the minimum and maximum frequency values and corresponding y values. It should also have methods `get_f_min(self)`, `get_f_max(self)`, `cent_per_value(self)`, and `freq_to_cents(self, frequency)`. The `cent_per_value(self)` method should return the y scale parameter in units of cents/y value, and the `freq_to_cents(self, frequency)` method should convert a given frequency to cents. The frequency conversion should be based on a logarithmic unit of tone intervals, with 1200 cents per octave.
"""

import math

def entrance(f_min, f_max, v_min, v_max, frequency):
    f_ratio = f_max / f_min
    v_ratio = v_max / v_min
    cent_per_val = 1200 * (math.log(f_ratio) / math.log(2)) / (math.log(v_ratio) / math.log(2))
    return 1200 * math.log(frequency / f_min) / math.log(2)