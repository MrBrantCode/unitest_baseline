"""
QUESTION:
Write a function `generate_setup_commands` that takes five parameters: `REPO_DIR`, `CONF_PATH`, `SITE_NAME`, `HOME`, and `APP_DIR`. The function should return a list of commands to be executed for setting up a Django application. The commands should include printing the values of `REPO_DIR`, `CONF_PATH`, `SITE_NAME`, `SITE_DIR`, and `APP_DIR`, changing the directory to `$HOME/BaseStack/fabric_files`, and executing the Fabric command `fab setup_django` with the arguments `conf_path` and `app_dir`. The `SITE_DIR` is a combination of `REPO_DIR` and `SITE_NAME`.
"""

def generate_setup_commands(REPO_DIR, CONF_PATH, SITE_NAME, HOME, APP_DIR):
    commands = [
        f'echo "REPO_DIR={REPO_DIR}"',
        f'echo "CONF_PATH={CONF_PATH}"',
        f'echo "SITE_NAME={SITE_NAME}"',
        f'echo "SITE_DIR={REPO_DIR}/{SITE_NAME}"',
        f'echo "APP_DIR={APP_DIR}"',
        f'cd {HOME}/BaseStack/fabric_files',
        f'fab setup_django:conf_path={CONF_PATH},app_dir={APP_DIR}'
    ]
    return commands