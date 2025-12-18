"""
QUESTION:
Write a function `generate_style_transfer_command` that takes in four parameters: `target` (the input target image file path), `output_prefix` (the prefix for the output files), `width` (the width of the output image), and `vgg_weights` (the file path to the VGG model weights). The function should return a command-line argument string following the format:
```
$TARGET $TARGET $TARGET \
out/$OUTPUT_PREFIX-texturized/$OUTPUT_PREFIX-Bp \
--analogy-layers='conv3_1,conv4_1' \
--scales=3 --analogy-w=0 \
--mode=brute --patch-size=3 \
--width=$WIDTH \
--vgg-weights=$VGG_WEIGHTS --output-full
```
"""

def generate_style_transfer_command(target: str, output_prefix: str, width: int, vgg_weights: str) -> str:
    command = f"{target} {target} {target} " \
              f"out/{output_prefix}-texturized/{output_prefix}-Bp " \
              f"--analogy-layers='conv3_1,conv4_1' " \
              f"--scales=3 --analogy-w=0 " \
              f"--mode=brute --patch-size=3 " \
              f"--width={width} " \
              f"--vgg-weights={vgg_weights} --output-full"
    return command