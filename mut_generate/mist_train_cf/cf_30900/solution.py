"""
QUESTION:
Implement the function `apply_trajectory_filter` that takes configuration parameters and a list of subcluster shapes as input, and filters the subcluster shapes based on the given criteria. The configuration parameters include `ComponentType`, `layerMask`, `maxNSat`, `maxTrimmedSizeDiffNeg`, `maxTrimmedSizeDiffPos`, and `seedCutMIPs`. The function should return the filtered subcluster shapes.

The configuration parameters are a dictionary where:
- `ComponentType` is a string indicating the type of trajectory filter component.
- `layerMask` is a dictionary specifying which detector layers to consider for filtering. The values are either a boolean indicating whether to consider all layers, or a list of specific layers.
- `maxNSat` is an integer indicating the maximum number of saturated strips allowed in a subcluster.
- `maxTrimmedSizeDiffNeg` and `maxTrimmedSizeDiffPos` are floating-point numbers indicating the maximum allowed difference in size for negatively and positively charged subclusters, respectively.
- `seedCutMIPs` is a floating-point number indicating the seed cut in minimum ionizing particles (MIPs).

Each subcluster shape has attributes `layer`, `num_strips`, and `charge`. The function should filter the subcluster shapes based on these attributes and the given configuration parameters.
"""

from typing import List

def apply_trajectory_filter(config_params, subcluster_shapes) -> List[dict]:
    filtered_shapes = []
    for shape in subcluster_shapes:
        if shape['layer'] in config_params['layerMask']:
            if isinstance(config_params['layerMask'][shape['layer']], bool):
                if config_params['layerMask'][shape['layer']]:
                    if (shape['num_strips'] <= config_params['maxNSat'] and
                            (shape['charge'] < 0 and shape['num_strips'] <= config_params['maxTrimmedSizeDiffNeg']) or
                            (shape['charge'] > 0 and shape['num_strips'] <= config_params['maxTrimmedSizeDiffPos']) or
                            (shape['charge'] == 0 and shape['num_strips'] <= config_params['seedCutMIPs'])):
                        filtered_shapes.append(shape)
            else:
                if shape['layer'] in config_params['layerMask'][shape['layer']]:
                    if (shape['num_strips'] <= config_params['maxNSat'] and
                            (shape['charge'] < 0 and shape['num_strips'] <= config_params['maxTrimmedSizeDiffNeg']) or
                            (shape['charge'] > 0 and shape['num_strips'] <= config_params['maxTrimmedSizeDiffPos']) or
                            (shape['charge'] == 0 and shape['num_strips'] <= config_params['seedCutMIPs'])):
                        filtered_shapes.append(shape)
    return filtered_shapes