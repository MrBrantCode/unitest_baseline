"""
QUESTION:
Create a function `generate_django_settings` that generates a Django settings file as a string. The function should take four parameters: `static_url`, `static_root`, `media_url`, and `media_root`. The generated settings file should be in the following format:
```python
from .base import *

STATIC_URL = '<static_url>'
STATIC_ROOT = '<static_root>'

MEDIA_URL = '<media_url>'
MEDIA_ROOT = '<media_root>'
```
Replace `<static_url>`, `<static_root>`, `<media_url>`, and `<media_root>` with the corresponding parameter values. The generated settings file should be properly formatted and ready for use in a Django project.
"""

def generate_django_settings(static_url, static_root, media_url, media_root):
    settings_template = f"""from .base import *

STATIC_URL = '{static_url}'
STATIC_ROOT = '{static_root}'

MEDIA_URL = '{media_url}'
MEDIA_ROOT = '{media_root}'
"""
    return settings_template