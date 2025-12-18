"""
QUESTION:
Create a function `configure_gerrit_trigger` that configures a Gerrit trigger for a Jenkins multibranch pipeline. The function should take three parameters: `server_name`, `project_name`, and `trigger_events`. It should return a string representing the Gerrit trigger configuration in the Jenkinsfile format. The trigger configuration should include the Gerrit server name, project name, and trigger events.
"""

def configure_gerrit_trigger(server_name, project_name, trigger_events):
    """
    Configures a Gerrit trigger for a Jenkins multibranch pipeline.

    Args:
        server_name (str): The name of the Gerrit server.
        project_name (str): The name of the Gerrit project.
        trigger_events (list): A list of Gerrit events that trigger the pipeline.

    Returns:
        str: The Gerrit trigger configuration in the Jenkinsfile format.
    """
    gerrit_config = "triggers {\n"
    gerrit_config += "  gerrit(\n"
    gerrit_config += "    serverName: '{}',\n".format(server_name)
    gerrit_config += "    gerritProjects: [[\n"
    gerrit_config += "      compareType: 'PLAIN',\n"
    gerrit_config += "      pattern: '{}'\n".format(project_name)
    gerrit_config += "      branches: [[\n"
    gerrit_config += "        compareType: 'ANT',\n"
    gerrit_config += "        pattern: '**'\n"
    gerrit_config += "      ]]\n"
    gerrit_config += "    ]],\n"
    gerrit_config += "    triggerOnEvents: [\n"
    for event in trigger_events:
        gerrit_config += "      $class: '{}',\n".format(event)
    gerrit_config = gerrit_config.rstrip(',\n') + "\n"
    gerrit_config += "    ]\n"
    gerrit_config += "  )\n"
    gerrit_config += "}\n"
    return gerrit_config