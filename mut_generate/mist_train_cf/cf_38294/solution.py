"""
QUESTION:
Write a Python function `generate_release_command` that generates a release command based on the given parameters. The function should take the following parameters: `project_name`, `project_dir`, `branch`, `web_root`, `git_protocol`, `git_host`, `git_port`, `git_user`, `group`, `user`, `charset`, `git_charset`, and `log_dir`. The function should return a string representing the release command with the placeholders replaced with the actual parameter values.
"""

def generate_release_command(project_name, project_dir, branch, web_root, git_protocol, git_host, git_port, git_user, group, user, charset, git_charset, log_dir):
    release_command = f'bash ${{RELEASE_EXCE}} release -p="{project_name}" --project-dir="{project_dir}" --branch="{branch}" --web-root="{web_root}" --git-protocol="{git_protocol}" --git-host="{git_host}" --git-port={git_port} --git-user="{git_user}" --group="{group}" --user="{user}" --charset="{charset}" --git-charset="{git_charset}" --log-dir="{log_dir}"'
    return release_command