"""
QUESTION:
Implement a class named `OnlineJudgeURLs` that has two methods: `get_problem_url(problem_code, contest_code)` and `get_contest_url(contest_code)`. The `get_problem_url` method should return a string representing the URL of a problem with the given problem code in a contest with the given contest code. The `get_contest_url` method should return a string representing the URL of a contest with the given contest code. Use Codeforces as the online judge platform. The URLs should be in the format "https://codeforces.com/contest/{contest_code}/problem/{problem_code}" and "https://codeforces.com/contest/{contest_code}" respectively.
"""

def entance(problem_code, contest_code):
    class CodeforcesURLs:
        def get_problem_url(self, problem_code, contest_code):
            return f"https://codeforces.com/contest/{contest_code}/problem/{problem_code}"

        def get_contest_url(self, contest_code):
            return f"https://codeforces.com/contest/{contest_code}"
    
    codeforces_urls = CodeforcesURLs()
    return codeforces_urls.get_problem_url(problem_code, contest_code), codeforces_urls.get_contest_url(contest_code)