"""
QUESTION:
Create a function `check_srid_has_meter_unit(srid: int) -> bool` that takes an integer `srid` as input and returns `True` if the given SRID uses the meter unit, and `False` otherwise, assuming the SRID is valid and exists in the system.
"""

def entrance(srid: int) -> bool:
    meter_unit_srids = {3857, 900913, 3785}  # Common SRIDs using meter unit
    return srid in meter_unit_srids