"""
QUESTION:
Create a function `generate_url_config` that generates the corresponding URL configuration in Django's URL patterns format. The function should take four parameters: 
- `url_pattern`: a string representing the URL pattern, e.g., `'^forgot-password$'`
- `view_name`: a string representing the name of the view, e.g., `'PasswordResetView.as_view(template_name='registration/password_forgot_form.html', email_template_name='email/email-password-forgot-link.txt', html_email_template_name='email/email-password-forgot-link.html', from_email=settings.DEFAULT_FROM_EMAIL)'`
- `url_name`: a string representing the name of the URL, e.g., `'forgot_password_v2'`
- `waffle_switch`: a string representing the waffle switch condition, e.g., `'login'`
 
The function should return a string representing the URL configuration in Django's URL patterns format, where the output is a string that can be used directly in Django's URL configuration, similar to `url(r'^forgot-password$', waffle_switch('login')(PasswordResetView.as_view(template_name='registration/password_forgot_form.html', email_template_name='email/email-password-forgot-link.txt', html_email_template_name='email/email-password-forgot-link.html', from_email=settings.DEFAULT_FROM_EMAIL)), name='forgot_password_v2'),`.
"""

def generate_url_config(url_pattern, view_name, url_name, waffle_switch):
    return f"url({url_pattern}, {waffle_switch}({view_name}), name='{url_name}'),"