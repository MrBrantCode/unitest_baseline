"""
QUESTION:
Write a function to exclude certain subdomains from a wildcard subdomain rule in Apache configuration, using the `.htaccess` file. The function should take a list of subdomains to exclude and modify the existing `.htaccess` rule to prevent rewriting for these subdomains. The existing rule rewrites all requests to `index.php` if the requested file or directory does not exist.
"""

def exclude_subdomains(subdomains):
    """
    This function generates Apache .htaccess rules to exclude certain subdomains 
    from a wildcard subdomain rule.

    Args:
        subdomains (list): A list of subdomains to exclude from the rule.

    Returns:
        str: The Apache .htaccess rules as a string.
    """

    rules = "RewriteEngine On\nRewriteBase /\n\n"

    # Add conditions to exclude each subdomain
    for subdomain in subdomains:
        rules += "# Exclude " + subdomain + "\n"
        rules += "RewriteCond %{HTTP_HOST} ^" + subdomain + "$ [NC]\n"
        rules += "RewriteRule .* - [L]\n\n"

    # Add the existing rule
    rules += "RewriteCond %{REQUEST_FILENAME} !-f\n"
    rules += "RewriteCond %{REQUEST_FILENAME} !-d\n"
    rules += "RewriteRule . /index.php [L]"

    return rules