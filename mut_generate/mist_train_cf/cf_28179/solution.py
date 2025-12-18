"""
QUESTION:
Implement the function `handleCORSRequest` that takes in `requestMethod` (string), `requestHeaders` (dictionary), and `allowedOrigins` (list of strings) and returns a dictionary representing the CORS headers for the server's response. The function should follow these rules: 

- For simple methods ("GET", "POST", "HEAD"), include the "Access-Control-Allow-Origin" header with the origin of the incoming request if it is in `allowedOrigins`.
- For preflight requests ("OPTIONS" method), include the "Access-Control-Allow-Origin" header with the origin of the incoming request if it is in `allowedOrigins`, and the "Access-Control-Allow-Methods" header with the allowed methods for the resource.
- Set the "Access-Control-Allow-Origin" header to "*" if the request does not specify a particular origin.
"""

def handleCORSRequest(requestMethod, requestHeaders, allowedOrigins):
    corsHeaders = {}
    
    if requestMethod in ["GET", "POST", "HEAD"]:
        origin = requestHeaders.get("Origin")
        corsHeaders["Access-Control-Allow-Origin"] = origin if origin in allowedOrigins else "*"
    elif requestMethod == "OPTIONS":
        origin = requestHeaders.get("Origin")
        corsHeaders["Access-Control-Allow-Origin"] = origin if origin in allowedOrigins else "*"
        corsHeaders["Access-Control-Allow-Methods"] = ", ".join(["GET", "POST", "PUT", "DELETE"])  # Replace with actual allowed methods
    
    return corsHeaders