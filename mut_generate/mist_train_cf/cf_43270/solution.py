"""
QUESTION:
Implement the `inferenceHierarchy` function to perform hierarchical inference on an input image using a given model and postprocessor. The function should refine the probability map with a Conditional Random Field (CRF) if a postprocessor and raw image are provided, and then use the refined probability map to generate a label map. The function takes in the following parameters: `model`, `image`, `raw_image=None`, `postprocessor=None`, `sizeThresh=1/9`, and `nIterations=10`. The function should return the generated label map.
"""

import numpy as np

def inferenceHierarchy(model, image, raw_image=None, postprocessor=None, sizeThresh=1/9, nIterations=10):
    _, _, H, W = image.shape

    # Image -> Probability map
    probs = model.predict_proba(image)

    # Refine the prob map with CRF
    if postprocessor and raw_image is not None:
        probs = postprocessor(raw_image, probs)

    # Generate label map
    labelmap = np.argmax(probs, axis=0)

    return labelmap