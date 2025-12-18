"""
QUESTION:
Design a function `load_testing_tool_selector` that recommends a suitable load testing tool based on the requirement of simulating multiple users accessing a web application from different locations and performing the same functionality at the same time. The tool should be able to handle four to six different users and provide insights on the application's performance under load.
"""

def load_testing_tool_selector(users: int) -> str:
    """
    Recommends a suitable load testing tool based on the requirement of simulating multiple users.

    Args:
    users (int): The number of users to be simulated.

    Returns:
    str: The recommended load testing tool.
    """
    
    if users >= 4 and users <= 6:
        # Apache JMeter can handle a large number of users and is suitable for this scenario
        return "Apache JMeter"
    elif users < 4:
        # For a small number of users, Locust can be a good option
        return "Locust"
    else:
        # For a very large number of users, LoadRunner or Gatling might be more suitable
        return "LoadRunner or Gatling"