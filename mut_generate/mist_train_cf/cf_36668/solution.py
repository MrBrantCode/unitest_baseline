"""
QUESTION:
Given two arrays `gas` and `cost`, where `gas` represents the amount of gas available at each station and `cost` represents the cost to travel from the i-th station to the (i+1)-th station, find the starting gas station index that allows you to travel around the circuit once in the clockwise direction without running out of gas. The circuit is a circular route where the last station is connected to the first station. Write a function `findStartingStation` that takes in `gas` and `cost` as input and returns the starting gas station index if a solution exists, otherwise return -1.
"""

from typing import List

def findStartingStation(gas: List[int], cost: List[int]) -> int:
    total_gas = 0
    total_cost = 0
    tank = 0
    start_station = 0

    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        tank += gas[i] - cost[i]
        if tank < 0:
            start_station = i + 1
            tank = 0

    return start_station if total_gas >= total_cost else -1