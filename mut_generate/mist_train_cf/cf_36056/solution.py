"""
QUESTION:
Create a function `generate_game_chart` that takes a dictionary containing music timing information as input. The dictionary is expected to have a key 'timings' that maps timestamps to BPM values. The function should return a chart in the format of a list of tuples, where each tuple contains an action name, a timestamp, and a BPM value. The action names should be in the format 'actionX', where X is a sequential number starting from 1.
"""

def generate_game_chart(music_timing_info):
    timings = music_timing_info['timings']
    chart = []
    action_count = 1
    for timestamp, bpm in timings.items():
        action_name = f'action{action_count}'
        chart.append((action_name, timestamp, bpm))
        action_count += 1
    return chart