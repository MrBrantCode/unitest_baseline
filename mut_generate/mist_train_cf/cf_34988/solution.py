"""
QUESTION:
Create a function `generate_open_command(server, secret, gid, alfred)` that generates the command to open a file in the correct application based on the provided parameters. The function should use the `server` object to retrieve the directory path and file path, encode the file path as UTF-8, and check if the file path exists on the local system. If the file path exists and `alfred` is True, generate AppleScript commands to search for the file in Alfred 2 and Alfred 3. If `alfred` is False, generate a command to open the file in the default application. If the file path does not exist, generate a command to open the directory path in the default application. The function should return the generated command as a string.
"""

import os

def generate_open_command(server, secret, gid, alfred):
    dir_path = server.tellStatus(secret, gid, ['dir'])['dir']
    file_path = server.getFiles(secret, gid)[0]['path'].encode('utf-8')

    if os.path.exists(file_path):
        if alfred:
            alfred_2_cmd = 'if application "Alfred 2" is running then tell application "Alfred 2" to search "%s"' % file_path
            alfred_3_cmd = 'if application "Alfred 3" is running then tell application "Alfred 3" to search "%s"' % file_path
            os_command = "osascript -e '%s' & osascript -e '%s'" % (alfred_2_cmd, alfred_3_cmd)
        else:
            os_command = 'open -R "%s"' % file_path
    else:
        os_command = 'open "%s" ' % dir_path

    return os_command