"""
QUESTION:
Write a function `parse_nmea_sentences(nmea_sentences: List[str]) -> Dict[str, Union[float, None]]` that takes a list of NMEA sentences as input and returns a dictionary containing the parsed depth and water temperature data. The function should handle two types of NMEA sentences: 
1. Depth (DPT) sentence: $IIDBT,,f,<depth>,M,,F 
2. Water temperature (MTW) sentence: $IIMTW,<temperature>,C 
and return a dictionary with the keys 'depth' and 'water_temperature' and corresponding values as floats if present, otherwise None.
"""

from typing import List, Dict, Union

def parse_nmea_sentences(nmea_sentences: List[str]) -> Dict[str, Union[float, None]]:
    parsed_data = {'depth': None, 'water_temperature': None}
    
    for sentence in nmea_sentences:
        if sentence.startswith('$IIDBT'):
            depth_index = sentence.find('f,')
            if depth_index != -1:
                depth_str = sentence[depth_index + 2 : sentence.find(',M', depth_index)]
                parsed_data['depth'] = float(depth_str) if depth_str else None
        elif sentence.startswith('$IIMTW'):
            temperature_index = sentence.find(',')
            if temperature_index != -1:
                temperature_str = sentence[temperature_index + 1 : sentence.find(',C')]
                parsed_data['water_temperature'] = float(temperature_str) if temperature_str else None
    
    return parsed_data