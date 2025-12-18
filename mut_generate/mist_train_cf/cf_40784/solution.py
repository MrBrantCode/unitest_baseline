"""
QUESTION:
Create a function `fileStructure` that generates a string representing an XML file structure for a drone control system. The function takes four parameters: `ip` (string), `port` (int), `drones` (list of strings), and `leds` (list of strings). The file structure should include IP and port information, arguments for each drone (URI and frame information), and LED information for each LED. The function should return the constructed file structure as a string.
"""

def fileStructure(ip, port, drones, leds):
    file_structure = f'<rosparam>\n  <param name="ip" value="{ip}" />\n  <param name="port" value="{port}" />\n  <node>\n'
    
    drone_args = "\n".join([
        f'    <arg name="uri{drone_number}" default="radio://0/80/2M/E7E7E7E7{drone_number}..." />\n    <arg name="frame{drone_number}" default="{drone}" />'
        for drone_number, drone in enumerate(drones)
    ])
    
    led_params = "\n".join([f'    <param name="led" value="{led}" />' for led in leds])
    
    file_structure += f'{drone_args}\n{led_params}\n  </node>\n</rosparam>'
    
    return file_structure