"""
QUESTION:
Implement the function `parse_data_packet(packet: bytes) -> List[float]` that takes a byte array `packet` representing a single data packet and returns a list of sensor readings as floating-point values. Each data packet consists of multiple 10-bit sensor readings packed into bytes. The function should extract and convert these readings to voltage values based on a 10-bit resolution and a 0 to 5 volts range, and return them in a list. The voltage values should be rounded to 3 decimal places.
"""

from typing import List

def parse_data_packet(packet: bytes) -> List[float]:
    sensor_readings = []
    for i in range(0, len(packet), 2):
        reading = (packet[i] << 8) | packet[i+1]
        voltage = (reading / 1023) * 5
        sensor_readings.append(round(voltage, 3))
    return sensor_readings