"""
QUESTION:
Configure Hadoop's Classpath for Seamless MapReduce Operation

Create a function `configure_hadoop_classpath` to set up the classpath for a Hadoop MapReduce operation, ensuring that the Java Virtual Machine (JVM) can locate and load required classes at runtime. Consider the impact of Hadoop versions and supplementary libraries on classpath settings.
"""

def configure_hadoop_classpath(classpath, jar_path):
    """
    Configure Hadoop's classpath to include a specific jar file.

    Args:
        classpath (str): The initial Hadoop classpath.
        jar_path (str): The path to the jar file to be added to the classpath.

    Returns:
        str: The updated classpath with the added jar file.
    """
    updated_classpath = f"{classpath}:{jar_path}"
    return updated_classpath