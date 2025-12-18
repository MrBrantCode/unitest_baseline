"""
QUESTION:
Implement a function `extract_autofocus_info` that takes a list of integers `af_info` representing autofocus information, the autofocus image width `af_image_width`, and the autofocus image height `af_image_height`. The function should return a tuple containing the number of autofocus points, a list of AFArea coordinates, and the direction of the Y axis based on the camera model. Assume the camera model is "EOS". 

Note: The `af_info` array contains the number of autofocus points as the first integer, and the AFArea coordinates are given in a system where 0,0 is the image center. The function should adjust the last Y coordinate of the AFArea coordinates based on the image height.
"""

def extract_autofocus_info(af_info: list, af_image_width: int, af_image_height: int) -> (int, list, str):
    num_af_points = af_info[0]  
    af_area_coordinates = [(af_info[i], af_info[i + 1]) for i in range(1, num_af_points * 2, 2)]  
    af_area_coordinates[-1] = (af_area_coordinates[-1][0], af_image_height // 2)  
    return num_af_points, af_area_coordinates, "upwards"  # Assuming camera model is "EOS"