"""
QUESTION:
Write a function named `get_iis_object_schema` that returns a list of all IIS objects, the objects they can be contained in, and their properties when configuring IIS through WMI or ADSI. The function should consider the different versions of IIS and return the relevant information for IIS 6.0 and IIS 7.0 and later versions.
"""

def get_iis_object_schema(iis_version):
    """
    Returns a list of all IIS objects, the objects they can be contained in, and their properties 
    when configuring IIS through WMI or ADSI.

    Args:
        iis_version (float): The version of IIS.

    Returns:
        list: A list of dictionaries containing IIS object information.
    """

    # Initialize an empty list to store IIS object schema
    iis_schema = []

    # IIS 6.0 schema
    if iis_version == 6.0:
        # Add IIS 6.0 objects to the schema list
        # Please refer to the IIS WMI Provider Reference for IIS 6.0
        iis_schema.append({
            "object_name": "IIsApplication",
            "contained_in": "IIsWebVirtualDir",
            "properties": ["AppPoolId", "AppPoolName", "AppPoolStatus"]
        })
        iis_schema.append({
            "object_name": "IIsWebServer",
            "contained_in": "IIsComputer",
            "properties": ["ServerComment", "ServerBindings"]
        })

    # IIS 7.0 and later versions schema
    elif iis_version >= 7.0:
        # Add IIS 7.0 and later versions objects to the schema list
        # Please refer to the IIS Administration Pack: WMI Provider
        iis_schema.append({
            "object_name": "ApplicationPool",
            "contained_in": "Computer",
            "properties": ["Name", "AutoStart", "Enable32BitAppOnWin64"]
        })
        iis_schema.append({
            "object_name": "WebServer",
            "contained_in": "Computer",
            "properties": ["ServerComment", "ServerBindings"]
        })

    return iis_schema