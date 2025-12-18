"""
QUESTION:
Implement a function `process_assets` that takes a dictionary `ASSET_RESOLUTION` containing asset-resolution pairs, a specified collateral asset `COLLATERAL_ASSET`, and a dictionary `SYNTHETIC_ASSET_MAP` mapping synthetic assets to their corresponding values. The function should return a list of assets that do not match the collateral asset and have their resolutions present in the synthetic asset map. Note that the asset names in the returned list must match the keys in the synthetic asset map.
"""

def process_assets(ASSET_RESOLUTION, COLLATERAL_ASSET, SYNTHETIC_ASSET_MAP):
    return [x for x in ASSET_RESOLUTION.keys() if x != COLLATERAL_ASSET and x in SYNTHETIC_ASSET_MAP]