"""
QUESTION:
Lisa just got a new math workbook.  A workbook contains exercise problems, grouped into chapters.  Lisa believes a problem to be special if its index (within a chapter) is the same as the page number where it's located.  The format of Lisa's book is as follows:

There are $n$ chapters in Lisa's workbook, numbered from $\mbox{1}$ to $n$.
The $i^{\mbox{th}}$ chapter has $arr\left[i\right]$ problems, numbered from $\mbox{1}$ to $arr\left[i\right]$.
Each page can hold up to $\boldsymbol{\mbox{k}}$ problems. Only a chapter's last page of exercises may contain fewer than $\boldsymbol{\mbox{k}}$ problems.
Each new chapter starts on a new page, so a page will never contain problems from more than one chapter.
The page number indexing starts at $\mbox{1}$.

Given the details for Lisa's workbook, can you count its number of special problems?

Example 

$arr=[4,2]$ 

$k=3$   

Lisa's workbook contains $ar r[1]=4$ problems for chapter $\mbox{1}$, and $arr[2]=2$ problems for chapter $2$.  Each page can hold $k=3$ problems.  

The first page will hold $3$ problems for chapter $\mbox{1}$.  Problem $\mbox{1}$ is on page $\mbox{1}$, so it is special.  Page $2$ contains only Chapter $\mbox{1}$, Problem $\begin{array}{c}4\end{array}$, so no special problem is on page $2$.  Chapter $2$ problems start on page $3$ and there are $2$ problems.  Since there is no problem $3$ on page $3$, there is no special problem on that page either.  There is $\mbox{1}$ special problem in her workbook.

Note: See the diagram in the Explanation section for more details.  

Function Description  

Complete the workbook function in the editor below.     

workbook has the following parameter(s):  

int n: the number of chapters       
int k: the maximum number of problems per page  
int arr[n]: the number of problems in each chapter  

Returns 

- int: the number of special problems in the workbook   

Input Format

The first line contains two integers $n$ and $\boldsymbol{\mbox{k}}$, the number of chapters and the maximum number of problems per page. 

The second line contains $n$ space-separated integers $arr\left[i\right]$ where $arr\left[i\right]$ denotes the number of problems in the $i^{\mbox{th}}$ chapter.

Constraints

$1\leq n,k,ar r[i]\leq100$

Sample Input
STDIN       Function
-----       --------
5 3         n = 5, k = 3
4 2 6 1 10  arr = [4, 2, 6, 1, 10]

Sample Output
4

Explanation

The diagram below depicts Lisa's workbook with $n=5$ chapters and a maximum of $k=3$ problems per page. Special problems are outlined in red, and page numbers are in yellow squares.

There are $\begin{array}{c}4\end{array}$ special problems and thus we print the number $\begin{array}{c}4\end{array}$ on a new line.
"""

def count_special_problems(n: int, k: int, arr: list) -> int:
    """
    Counts the number of special problems in Lisa's workbook.

    A problem is considered special if its index (within a chapter) is the same as the page number where it's located.

    Parameters:
    - n (int): The number of chapters.
    - k (int): The maximum number of problems per page.
    - arr (list): A list of integers where each integer represents the number of problems in each chapter.

    Returns:
    - int: The number of special problems in the workbook.
    """
    special_count = 0
    current_page = 1

    for chapter in range(n):
        problems_in_chapter = arr[chapter]
        for problem_index in range(1, problems_in_chapter + 1):
            if problem_index == current_page:
                special_count += 1
            if problem_index % k == 0 or problem_index == problems_in_chapter:
                current_page += 1

    return special_count