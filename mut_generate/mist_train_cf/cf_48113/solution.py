"""
QUESTION:
Write a function named `find_default_session_store_location` that determines the default location where Tomcat stores its session files when `server.servlet.session.store-dir` is not specified.
"""

def find_default_session_store_location(tomcat_home):
    """
    Determines the default location where Tomcat stores its session files.

    Args:
    tomcat_home (str): The home directory of the Tomcat installation.

    Returns:
    str: The default location where Tomcat stores its session files.
    """
    return f"{tomcat_home}/work/Catalina/localhost/_SESSIONS.ser"