"""
QUESTION:
Write a function named `process_command` that takes two parameters: an input string and the number of GitHub stars. The input string is expected to contain a range of GitHub stars and a command to execute, separated by a newline character. The range of stars is denoted by `<gh_stars>x-y` where x and y are integers, and the command is expected to contain `$1` as a placeholder for the number of stars. The function should parse the input string, check if the number of stars falls within the specified range, and return the command with the placeholder replaced if it does. If the number of stars is out of range, the function should return "Out of range".
"""

def process_command(input_str, stars):
    range_str, command = input_str.split('\n')
    range_start, range_end = map(int, range_str.split('<gh_stars>')[1].split('-'))
    if range_start <= stars <= range_end:
        return command.replace('$1', str(stars))
    else:
        return "Out of range"