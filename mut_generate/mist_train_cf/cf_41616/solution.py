"""
QUESTION:
Implement a Python function `simulate_reboot` that takes in a list of processes and their respective execution times, and the time taken to reboot the system. The function should return the total time taken for the reboot process, which involves running all processes once and then running them again in reverse order.

The function should take two parameters: 
- `processes`: a list of tuples, where each tuple contains a process name (string) and its execution time (integer).
- `reboot_time`: an integer representing the time taken to reboot the system.

The total execution time for the reboot is the sum of the execution times of all processes in the original order, plus the sum of the execution times of all processes in the reverse order, plus the reboot time.
"""

def simulate_reboot(processes, reboot_time):
    total_time = sum(time for _, time in processes)  # Calculate the total time for original execution
    total_time *= 2  # Double the total time for original and reverse execution
    total_time += reboot_time  # Add the reboot time

    return total_time