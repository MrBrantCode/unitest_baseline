"""
QUESTION:
Write a function `getWaterPipesStatus(pipes)` that takes a list of water pipes as input and returns a list of dictionaries, where each dictionary contains the status, location, priority, and estimated repair time of a pipe that needs maintenance or repair. The priority and estimated repair time should be calculated based on the daily water requirement of the consumers supplied by the pipe and the historical data of pipe failures in the area. Assume that each pipe object has methods `needsMaintenanceOrRepair()`, `getDailyWaterRequirement()`, `getHistoricalData()`, and `getLocation()`.
"""

def entrance(pipes):
    """
    Returns the status, location, priority, and estimated repair time of water pipes that need maintenance or repair.
    """
    result = []
    for pipe in pipes:
        if pipe.needsMaintenanceOrRepair():
            dailyWaterRequirement = pipe.getDailyWaterRequirement()
            historicalData = pipe.getHistoricalData()
            priority = dailyWaterRequirement / 1000.0 # Higher water requirement means higher priority
            repairTime = 1.0 / (1.0 + historicalData) # Higher historical data means longer repair time
            result.append({
                "status": "Needs maintenance or repair",
                "location": pipe.getLocation(),
                "priority": priority,
                "estimatedRepairTime": repairTime
            })
    return result