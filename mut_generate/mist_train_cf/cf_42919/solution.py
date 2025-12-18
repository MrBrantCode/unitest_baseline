"""
QUESTION:
Write a function `stations_highest_rel_level(stations, N)` that takes a list of station objects `stations` and an integer `N`, and returns a list of the `N` stations with the highest relative water levels, provided that the station's typical range is consistent, the latest water level is not None, and the relative water level is greater than a certain tolerance. The relative water level for each station is calculated using the `relative_water_level()` method of the station object. The returned list should be sorted in descending order of relative water levels.
"""

def stations_highest_rel_level(stations, N, tol):
    return sorted([(station, station.relative_water_level()) 
                   for station in stations 
                   if station.typical_range_consistent() 
                   and station.latest_level is not None 
                   and station.relative_water_level() > tol], 
                  key=lambda x: x[1], reverse=True)[:N]