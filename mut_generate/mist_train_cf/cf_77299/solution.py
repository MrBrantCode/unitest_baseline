"""
QUESTION:
Combine Multiple Commits into One. Implement a function `combine_commits` that takes a number `n` as input, combines the last `n` commits into one without losing any modifications, and returns a string describing the steps to achieve this. The function should also explain the difference between 'git rebase' and 'git merge', their potential complications, and the circumstances where each command would yield the greatest benefits.
"""

def combine_commits(n):
    """
    Combine the last n commits into one without losing any modifications.

    Args:
    n (int): The number of commits to combine.

    Returns:
    str: A string describing the steps to achieve this and explaining the difference between 'git rebase' and 'git merge'.
    """
    steps = f"To combine the last {n} commits into one without losing any modifications, use 'git rebase' in interactive mode (-i) with a commit hash, like this: git rebase -i HEAD~{n}.\n"
    steps += "This will open the editor listing the last 'n' commits with the word 'pick' before each one. Replacing 'pick' with 'squash' or 's' will tell Git to squash that commit into the previous one.\n"
    steps += "Once you've marked the commits to squash, you can save and close the editor. Git will then combine all the changes into one commit and bring up another editor for you to create a new commit message.\n\n"

    difference = "Distinguishing between 'git rebase' and 'git merge':\n"
    difference += "1. Git Merge: This command is primarily used to combine the work of two different branches. It creates a new commit in the process, keeping the commit history intact but can compel a non-linear, complex commit history.\n"
    difference += "2. Git Rebase: This command, on the other hand, puts the changes from the current branch onto another base. It does not create a new commit but modifies the commit history giving a linear, simplified commit history.\n\n"

    complications = "Comparing their potential complications:\n"
    complications += "1. For 'git merge', if you have a complicated history and numerous branches, merge commit can pollute your history and make it harder to understand the project's progress.\n"
    complications += "2. With 'git rebase', if mistakes are made during the rebase, it becomes challenging to trace back the error as rebase alters the commit history.\n\n"

    usage = "Both commands should be used under appropriate circumstances:\n"
    usage += "1. Git Merge works best when you want to integrate code from one branch into another without affecting the commit history of the two branches.\n"
    usage += "2. Git Rebase is best used when you are working on a feature branch and need to incorporate updates from the main branch without cluttering your commit history with merge commits.\n\n"

    hazards_and_advantages = "Regarding potential hazards and advantages:\n"
    hazards_and_advantages += "1. The primary risk with 'rebase' is it can confuse the commit history if not handled carefully as it essentially rewrites the commit history.\n"
    hazards_and_advantages += "2. The benefits of 'rebase' include a clean, linear commit history, which makes it easier for team members to understand the history and progress.\n"
    hazards_and_advantages += "3. The main hazard with 'merge' is it can lead to a messier commit history due to numerous merge commits.\n"
    hazards_and_advantages += "4. Despite this, the benefit of 'merge' is it preserves the exact historical commit information and the context around changes, which some teams may find beneficial.\n"

    return steps + difference + complications + usage + hazards_and_advantages