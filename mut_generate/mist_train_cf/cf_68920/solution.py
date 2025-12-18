"""
QUESTION:
Write a function `externalize_config` to separate the configuration of an application from its EAR file in Glassfish v2. The function should describe how to externalize the configuration of an EJB application by using JNDI Resources, allowing configuration changes to be made without rebuilding and redeploying the application. The application restart is required after changing the JNDI entries.
"""

def externalize_config(ejb_config):
    """
    Externalize the configuration of an EJB application by using JNDI Resources.

    Args:
    ejb_config (dict): A dictionary containing the EJB configuration.

    Returns:
    dict: The externalized EJB configuration.
    """
    # Add configurable parameters in your sun-ejb-jar.xml file and specify their values in your Glassfish v2 Server for the JNDI entries.
    jndi_resources = {}
    for key, value in ejb_config.items():
        # Change your EJBs to lookup the configurable parameters through JNDI.
        jndi_resources[key] = f"java:comp/env/{key}"
    
    # Define these parameters in the Glassfish v2 admin console or using asadmin tool (create-jndi-resource or create-custom-resource).
    return jndi_resources