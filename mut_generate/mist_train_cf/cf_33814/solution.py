"""
QUESTION:
Implement a function `parse_output` that takes a string `output` as input, where the string is in the format 'Ping: <ping_time> ms\nDownload: <download_speed> <unit>\nUpload: <upload_speed> <unit>'. The function should return a tuple containing the ping time (in milliseconds), download speed (in Kbit/s), and upload speed (in Kbit/s). The input string will always be in the specified format, and the download and upload speeds will be in either 'bit/s' or 'Kbit/s'.
"""

def parse_output(output):
    lines = output.split('\n')
    ping_time = float(lines[0].split(': ')[1].split(' ms')[0])
    download_speed = float(lines[1].split(': ')[1].split(' ')[0])
    upload_speed = float(lines[2].split(': ')[1].split(' ')[0])

    if 'Kbit/s' in lines[1]:
        download_speed *= 1000
    if 'Kbit/s' in lines[2]:
        upload_speed *= 1000

    return ping_time, download_speed, upload_speed