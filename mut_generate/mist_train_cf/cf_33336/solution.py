"""
QUESTION:
Write a function `parse_keypoint_config(config)` that takes a dictionary `config` representing the configuration settings for a keypoint detection module as input. The function should return a dictionary containing the extracted keypoint detection settings. The returned dictionary should include the following keys and their corresponding values: 
- `type`: The type of the keypoint detection head.
- `output_heatmaps`: A boolean indicating whether output heatmaps are enabled.
- `keypoint_decoder_type`: The type of the keypoint decoder.
- `num_convs`: The number of convolutional layers in the keypoint head.
- `in_channels`: The number of input channels for the keypoint head.
- `features_size`: A list containing the sizes of features for the keypoint head.
- `conv_out_channels`: The number of output channels for the convolutional layers.
- `num_keypoints`: The number of keypoints to be detected.
- `loss_keypoint_type`: The type of loss function for keypoint detection.
- `loss_weight`: The weight assigned to the loss function.
If a key is not present in the input dictionary, the corresponding value in the returned dictionary should be set to `None`.
"""

def parse_keypoint_config(config: dict) -> dict:
    keypoint_settings = {
        'type': config.get('type', None),
        'output_heatmaps': config.get('output_heatmaps', None),
        'keypoint_decoder_type': config.get('keypoint_decoder', {}).get('type', None),
        'num_convs': config.get('keypoint_head', {}).get('num_convs', None),
        'in_channels': config.get('keypoint_head', {}).get('in_channels', None),
        'features_size': config.get('keypoint_head', {}).get('features_size', None),
        'conv_out_channels': config.get('keypoint_head', {}).get('conv_out_channels', None),
        'num_keypoints': config.get('keypoint_head', {}).get('num_keypoints', None),
        'loss_keypoint_type': config.get('keypoint_head', {}).get('loss_keypoint', {}).get('type', None),
        'loss_weight': config.get('keypoint_head', {}).get('loss_keypoint', {}).get('loss_weight', None)
    }
    return keypoint_settings