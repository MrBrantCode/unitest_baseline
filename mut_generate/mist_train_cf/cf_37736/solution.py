"""
QUESTION:
Write a Python function `calculate_effective_strides(backbone_shape, cfg)` that takes in two parameters:
- `backbone_shape` (dict): A dictionary containing information about the backbone network's shape, where the keys are the feature names and the values are objects containing stride and channel information.
- `cfg` (object): An object containing the model configuration, including the RESNETS.RES5_DILATION parameter and the MODEL.RESNETS.MULTI_STRIDES parameter.

The function should calculate the effective strides for feature extraction based on the following rules:
1. If `cfg.MODEL.RESNETS.MULTI_STRIDES` is True, the effective strides should be the minimum of the original strides and the feature strides from the `backbone_shape`.
2. If `cfg.MODEL.RESNETS.RES5_DILATION` is 2, the effective stride for the last layer should be halved.

The function should return a list of effective strides corresponding to each feature in the `backbone_shape` dictionary.
"""

def calculate_effective_strides(backbone_shape, cfg):
    effective_strides = []
    for i, f in enumerate(backbone_shape.keys()):
        if cfg.MODEL.RESNETS.MULTI_STRIDES:
            effective_strides.append(min(backbone_shape[f]['stride'], cfg.MODEL.RESNETS.BASE_STRIDE * 2 ** i))
        else:
            effective_strides.append(cfg.MODEL.RESNETS.BASE_STRIDE * 2 ** i)

    if cfg.MODEL.RESNETS.RES5_DILATION == 2:
        effective_strides[-1] = effective_strides[-1] // 2

    return effective_strides