"""
QUESTION:
Implement the function `simulateCircuitVoltage` to numerically solve the differential equation of a simple electrical circuit. The function should calculate the voltage across the capacitor as a function of time given the circuit parameters and a numerical integration method.

The function takes the following parameters:
- `vs` (float): the voltage source
- `r0` (float): the resistance of the series resistor
- `rl` (float): the resistance of the parallel resistor
- `rc` (float): the capacitance of the capacitor
- `initialVoltage` (float): the initial voltage across the capacitor
- `timeStep` (float): the time step for the numerical integration
- `totalTime` (float): the total time for the simulation

The function should return a list of tuples, where each tuple contains the time and the corresponding voltage across the capacitor.
"""

def simulateCircuitVoltage(vs, r0, rl, rc, initialVoltage, timeStep, totalTime):
    voltage = initialVoltage
    time = 0
    result = [(time, voltage)]

    while time < totalTime:
        dVc_dt = (vs - voltage) / r0 - voltage / rl
        voltage += dVc_dt * timeStep
        time += timeStep
        result.append((time, voltage))

    return result