"""
QUESTION:
Convert a CVS repository to an SVN repository and rename branches using cvs2svn tool. Write a function to create an options file for cvs2svn that will rename branches according to the following rules: CVS HEAD becomes a normal branch, CVS branchA becomes SVN trunk, and other branches are renamed as specified. The function should take the path to the CVS repository, the path to the future SVN repository, and a dictionary of branch mappings as input. The function should output the content of the options file. 

Restrictions: The cvs2svn tool is used for the conversion. The CVS and SVN repositories are on the same Linux machine.
"""

def create_cvs2svn_options(cvs_repo_path, svn_repo_path, branch_mappings):
    """
    Creates the content of an options file for cvs2svn that renames branches according to the given rules.
    
    Parameters:
    cvs_repo_path (str): The path to the CVS repository.
    svn_repo_path (str): The path to the future SVN repository.
    branch_mappings (dict): A dictionary of branch mappings.
    
    Returns:
    str: The content of the options file.
    """
    options_content = ""
    options_content += "# Convert CVS HEAD to a normal branch\n"
    options_content += f"set_project(':trunk', '{cvs_repo_path}', '{svn_repo_path}/trunk')\n"
    options_content += "# Convert CVS branchA to SVN trunk\n"
    options_content += f"set_project(':branch:branchA', '{cvs_repo_path}', '{svn_repo_path}/branches/trunk')\n"
    
    for cvs_branch, svn_branch in branch_mappings.items():
        options_content += f"# Convert CVS {cvs_branch} to SVN {svn_branch}\n"
        options_content += f"set_project(':branch:{cvs_branch}', '{cvs_repo_path}', '{svn_repo_path}/branches/{svn_branch}')\n"
    
    return options_content