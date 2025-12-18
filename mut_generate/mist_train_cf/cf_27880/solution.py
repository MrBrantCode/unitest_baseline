"""
QUESTION:
Create a function `create_user_command` that takes in six parameters: `username` (string), `system_user` (boolean), `create_home` (boolean), `shell` (string), `group` (boolean), and `login_disabled` (boolean). The function should return a string representing a Linux user creation command based on the provided parameters. The command should use the `adduser` command and include flags for system user, home directory creation, shell, group creation, and login status. The order of the parameters in the command does not matter.
"""

def create_user_command(username, system_user, create_home, shell, group, login_disabled):
    command = 'sudo adduser'
    if system_user:
        command += ' --system'
    if not create_home:
        command += ' --no-create-home'
    if shell:
        command += f' --shell {shell}'
    if group:
        command += ' --group'
    if login_disabled:
        command += ' --disabled-login'
    command += f' {username}'
    return command