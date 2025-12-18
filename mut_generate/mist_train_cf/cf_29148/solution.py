"""
QUESTION:
Implement a function `my_key(group, request, allowed_ips)` that validates a client's IP address against a list of allowed IP addresses for a specific group. The function should extract the real IP address from the request's metadata using the key `'HTTP_X_FORWARDED_FOR'` and compare it with the list of allowed IP addresses for the given group. If the extracted IP address is found in the list, return a success message; otherwise, return an error message. 

The function should take three parameters: `group` (the group to check the IP address against), `request` (the HTTP request containing the client's IP address in its metadata), and `allowed_ips` (a dictionary mapping groups to their respective lists of allowed IP addresses). The function should return a string message indicating whether access is granted or denied.
"""

def validate_ip(group, request, allowed_ips):
    try:
        real_ip = request.META.get('HTTP_X_FORWARDED_FOR')
        if real_ip:
            real_ip = real_ip.split(',')[0].strip()  # Extract the first IP if multiple IPs are present
            if real_ip in allowed_ips.get(group, []):
                return f"Access granted for {group} group from IP {real_ip}"
            else:
                return f"Access denied for {group} group from IP {real_ip}"
        else:
            return "Unable to retrieve client's IP address"
    except Exception as e:
        return f"Error occurred: {str(e)}"