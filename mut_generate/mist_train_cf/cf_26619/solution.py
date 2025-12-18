"""
QUESTION:
Implement a `calibrate` function that takes a string `device` representing the type of device being calibrated and a numerical value `target` representing the desired calibration target. The function should return a string indicating whether the calibration was successful or not. The function should support calibration processes for Thermometer, Scale, and Barometer devices, each with its own acceptable range for calibration: 0.1 for Thermometer (around 25.0), 0.01 for Scale (around 0.0), and 0.1 for Barometer (around 1013.25).
"""

def calibrate(device, target):
    calibration_ranges = {
        "Thermometer": {"target": 25.0, "range": 0.1},
        "Scale": {"target": 0.0, "range": 0.01},
        "Barometer": {"target": 1013.25, "range": 0.1},
    }
    
    if device in calibration_ranges:
        if abs(target - calibration_ranges[device]["target"]) < calibration_ranges[device]["range"]:
            return "Calibration successful"
        else:
            return "Calibration failed"
    else:
        return "Device not supported"