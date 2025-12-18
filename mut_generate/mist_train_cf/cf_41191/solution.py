"""
QUESTION:
Implement a function `convertStdDeviceToHubDevice` that takes a dictionary `std_device` as input and returns a dictionary representing the corresponding hub device. The input dictionary `std_device` contains the following keys: "id", "serial", "fitManufacturer", "fitDevice", "model", "firmware", and "user". The output dictionary should include the following keys: "id", "serial", "manufacturer" with a fixed value "Decathlon", "model", "firmware", and "user". If "fitDevice" in the input dictionary is not None, it should also be included in the output dictionary.
"""

def convertStdDeviceToHubDevice(std_device):
    hub_device = {
        "id": std_device["id"],
        "serial": std_device["serial"],
        "manufacturer": "Decathlon",
        "model": std_device["model"],
        "firmware": std_device["firmware"],
        "user": std_device["user"]
    }
    if std_device["fitDevice"] is not None:
        hub_device["fitDevice"] = std_device["fitDevice"]
    return hub_device