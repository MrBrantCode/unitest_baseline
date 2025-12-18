"""
QUESTION:
Function: Reconfigure the classpath for a Hadoop MapReduce operation. 

Configure the classpath to include the necessary Hadoop JAR files and configuration files, while considering the specific requirements of the Hadoop version and any supplementary libraries being used. The function should ensure the correct arrangement of the classpath to prevent a 'ClassNotFound' exception.

Restrictions: The solution should account for different Hadoop versions, correctly built JAR files, and the interplay between Hadoop configuration files and supplementary libraries.
"""

import os

def configure_classpath(hadoop_version, hadoop_dir, supplementary_jars=None):
    """
    Configures the classpath for a Hadoop MapReduce operation.

    Args:
        hadoop_version (str): The version of Hadoop being used.
        hadoop_dir (str): The directory where Hadoop is installed.
        supplementary_jars (list): A list of paths to supplementary JAR files.

    Returns:
        str: The updated classpath.
    """

    # Initialize the classpath with the Hadoop JAR files and configuration files
    classpath = os.path.join(hadoop_dir, 'lib', '*')
    classpath += ':' + os.path.join(hadoop_dir, 'conf')

    # Add the supplementary JAR files to the classpath if provided
    if supplementary_jars:
        for jar in supplementary_jars:
            classpath += ':' + jar

    # Adjust the classpath according to the Hadoop version
    if hadoop_version == '1.0':
        classpath += ':' + os.path.join(hadoop_dir, 'lib', 'hadoop-core-1.0.jar')
    elif hadoop_version == '2.0':
        classpath += ':' + os.path.join(hadoop_dir, 'lib', 'hadoop-common-2.0.jar')

    return classpath