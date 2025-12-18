"""
QUESTION:
Create a function `configure_jupyter_server` that takes the following parameters: 
- `token`: a string representing the token for authentication (empty string means no token is required)
- `password`: a string representing the password for authentication (empty string means no password is required)
- `open_browser`: a boolean indicating whether to open the browser automatically when the Jupyter Notebook server starts
- `port`: an integer representing the port on which the Jupyter Notebook server should run
- `allow_remote_access`: a boolean indicating whether remote access to the server should be allowed
- `allow_origin_pat`: a string representing the regular expression pattern for allowed origins

The function should return a string representing the configuration settings for the Jupyter Notebook server based on the input parameters. The configuration settings should be in the format: 
c.NotebookApp.token = '{token}'
c.NotebookApp.password = '{password}'
c.NotebookApp.open_browser = {open_browser}
c.NotebookApp.port = {port}
c.NotebookApp.allow_remote_access = {allow_remote_access}
c.NotebookApp.allow_origin_pat = '{allow_origin_pat}'
"""

def configure_jupyter_server(token, password, open_browser, port, allow_remote_access, allow_origin_pat):
    config_settings = f'''
c.NotebookApp.token = '{token}'
c.NotebookApp.password = '{password}'
c.NotebookApp.open_browser = {str(open_browser).lower()}
c.NotebookApp.port = {port}
c.NotebookApp.allow_remote_access = {str(allow_remote_access).lower()}
c.NotebookApp.allow_origin_pat = '{allow_origin_pat}'
'''
    return config_settings