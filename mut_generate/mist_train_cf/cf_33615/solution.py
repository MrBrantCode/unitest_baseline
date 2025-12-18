"""
QUESTION:
Implement a function `process_commands` that simulates the behavior of a system by executing a list of commands in the given order. The function takes a list of commands as input and returns the final state of the system after processing all the commands. The commands can be one of the following:

* `beetle_ssh 'Beetle --SetGpioDirection "$gpio" OUT'`: Configures the microcontroller to set the GPIO direction to output.
* `beetle_ssh 'Beetle --SetGpio "$gpio" HIGH'`: Sets the GPIO pin on the microcontroller to a high state.
* `sleep $kernel_hotplug_time`: Pauses the execution for a specified duration (no action needed for simulation).
* `$rootdir/scripts/setup.sh reset`: Resets the setup (no action needed for simulation).
* `blk_list1=$(lsblk -d --output NAME | grep "^nvme")`: Retrieves a list of block devices connected to the system (returns a predefined list of devices for simulation).
* `remove_device`: Removes a device from the system.

The function should keep track of the GPIO direction, GPIO state, and devices connected, and return these values as the final system state. The input commands are provided as a list of strings.
"""

from typing import List

def process_commands(commands: List[str]) -> dict:
    gpio_direction = "IN"
    gpio_state = "LOW"
    devices_connected = []

    for command in commands:
        if 'Beetle --SetGpioDirection' in command:
            gpio_direction = "OUT"
        elif 'Beetle --SetGpio' in command:
            gpio_state = "HIGH"
        elif 'lsblk -d --output NAME | grep "^nvme"' in command:
            devices_connected = ["nvme1", "nvme2", "nvme3"]  # Simulate retrieval of block devices
        elif 'remove_device' in command:
            devices_connected = []  # Simulate device removal

    return {
        "gpio_direction": gpio_direction,
        "gpio_state": gpio_state,
        "devices_connected": devices_connected
    }