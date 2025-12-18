"""
QUESTION:
Create a function `to_code(config)` that takes a dictionary `config` as input and returns a string representing the code for initializing a web server. The function should initialize the web server with the port number obtained from the `config` dictionary and set the CSS URL and/or JS URL if they are present in the dictionary. The function should handle the following cases: 
- Initialize the web server with the port number obtained from `config['CONF_PORT']`.
- Set the CSS URL if `config['CONF_CSS_URL']` is present.
- Set the JS URL if `config['CONF_JS_URL']` is present.

The code should follow the pattern where the web server is initialized with `App.init_web_server()`, and `Pvariable()` and `add()` are used to set the ID, CSS URL, and JS URL. The ID should be obtained from `config['CONF_ID']`.
"""

def to_code(config):
    code = f"rhs = App.init_web_server({config['CONF_PORT']})\n"
    code += f"web_server = Pvariable('{config['CONF_ID']}', rhs)\n"
    if 'CONF_CSS_URL' in config:
        code += f"add(web_server.set_css_url('{config['CONF_CSS_URL']}'))\n"
    if 'CONF_JS_URL' in config:
        code += f"add(web_server.set_js_url('{config['CONF_JS_URL']}'))"
    return code