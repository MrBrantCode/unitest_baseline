"""
QUESTION:
To write a research paper, you should definitely follow the structured format. This format, in many cases, is strictly defined, and students who try to write their papers have a hard time with it.

One of such formats is related to citations. If you refer several pages of a material, you should enumerate their page numbers in ascending order. However, enumerating many page numbers waste space, so you should use the following abbreviated notation:

When you refer all pages between page a and page b (a < b), you must use the notation "a-b". For example, when you refer pages 1, 2, 3, 4, you must write "1-4" not "1 2 3 4". You must not write, for example, "1-2 3-4", "1-3 4", "1-3 2-4" and so on. When you refer one page and do not refer the previous and the next page of that page, you can write just the number of that page, but you must follow the notation when you refer successive pages (more than or equal to 2). Typically, commas are used to separate page numbers, in this problem we use space to separate the page numbers.

You, a kind senior, decided to write a program which generates the abbreviated notation for your junior who struggle with the citation.

Constraints

* 1 ≤ n ≤ 50

Input

Input consists of several datasets.

The first line of the dataset indicates the number of pages n.

Next line consists of n integers. These integers are arranged in ascending order and they are differ from each other.

Input ends when n = 0.

Output

For each dataset, output the abbreviated notation in a line. Your program should not print extra space. Especially, be careful about the space at the end of line.

Example

Input

5
1 2 3 5 6
3
7 8 9
0


Output

1-3 5-6
7-9
"""

def generate_abbreviated_citation(pages):
    if not pages:
        return ""
    
    ans = []
    start = pages[0]
    end = pages[0]
    
    for i in range(1, len(pages)):
        if pages[i] == end + 1:
            end = pages[i]
        else:
            if start == end:
                ans.append(str(start))
            else:
                ans.append(f"{start}-{end}")
            start = pages[i]
            end = pages[i]
    
    if start == end:
        ans.append(str(start))
    else:
        ans.append(f"{start}-{end}")
    
    return ' '.join(ans)