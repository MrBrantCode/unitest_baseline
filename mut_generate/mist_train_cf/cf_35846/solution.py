"""
QUESTION:
Create a function `applyStripSubClusterShapeSeedFilter` that takes two parameters: `subcluster`, a list of strip charges, and `params`, a dictionary containing filter parameters. The function should return `True` if the subcluster meets the filter criteria based on the provided parameters and `False` otherwise.

The filter parameters are: 
- `minNStrips` (int): Minimum number of strips in the subcluster.
- `maxNStrips` (int): Maximum number of strips in the subcluster.
- `minGoodStripCharge` (double): Minimum charge of a good strip.
- `maxGoodStripCharge` (double): Maximum charge of a good strip.
- `minNStripsWithGoodCharge` (int): Minimum number of strips with good charge.

The function should check if the number of strips in the subcluster falls within the specified range and if the number of strips with good charge meets the minimum requirement.
"""

def applyStripSubClusterShapeSeedFilter(subcluster, params):
    if params['minNStrips'] <= len(subcluster) <= params['maxNStrips']:
        good_strips = [strip for strip in subcluster if params['minGoodStripCharge'] <= strip <= params['maxGoodStripCharge']]
        if len(good_strips) >= params['minNStripsWithGoodCharge']:
            return True
    return False