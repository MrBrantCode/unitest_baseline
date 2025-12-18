"""
QUESTION:
To change the log directory in JBoss without modifying domain.xml and host.xml, you need to modify the `JBOSS_LOG_DIR` variable in the standalone(.sh/.bat) or domain(.sh/.bat) script files in the JBoss /bin directory. The function is to change the `JBOSS_LOG_DIR` environment variable so that `Jboss.server.log.dir` can pick up this new log directory.
"""

import os

def change_jboss_log_dir(log_dir):
    os.environ['JBOSS_LOG_DIR'] = log_dir
    return os.getenv('JBOSS_LOG_DIR')