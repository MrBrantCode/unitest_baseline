"""
QUESTION:
Create a program to simulate the gradual increase of temperature in a tank based on the equation T = T0 × e^(k × t) over time. The program should be able to heat the temperature to a specific value (Treo) while calculating the time it takes to achieve the target temperature. The program should have a function `simulate_temperature_increase(T0, k, time_interval, initial_time, Treo)` to simulate the temperature increase, where T0 is the initial temperature at t=0, k is a constant that determines the rate of temperature increase, time_interval is the interval at which the temperature will be calculated and printed, initial_time is the initial time, and Treo is the target temperature. The function should continuously calculate and print the temperature at the specified time intervals until the target temperature is reached and return the total time it took to reach the target temperature.
"""

import math

def simulate_temperature_increase(T0, k, time_interval, initial_time, Treo):
    current_time = initial_time
    current_temp = T0

    while current_temp < Treo:
        current_temp = T0 * math.exp(k * (current_time - initial_time))
        print(f"Temperature at {current_time} seconds: {current_temp:.2f}")

        if current_temp >= Treo:
            break

        current_time += time_interval

    total_time = current_time - initial_time
    return total_time