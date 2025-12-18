"""
QUESTION:
Xavier challenges one of his friend to perform some crazy string functions by giving him some words and each word basically denotes a type of string function which his friend has to perform.

WORDS WITH THEIR MEANING:-

Wordrev n->To arrange each words of the string in reverse order.The last   letter n
denotes upto which letter the words are to be reversed in the   string. For example:-the given string is my name is xavier,the given task is Wordrev 3.Then the output must be ym eman si xavier.The 3 words are reversed because the last letter is 3 that is the task is performed for 3 words,and the remaining are simply dispalyed same as they were.

subpalin n->To find the nth palindrome substring present in the given string.Here n denotes the nth palindrome substring. For eg the string is xyzbabmadamh,the task is subpalin 2.The output must be madam which is the substring of given input string."ababa" is also a palin substring but it   is not the second,it was the first substring.

sortword n->To sort the given string words alphabetically.The letter n denotes the step upto which the sorting is to be done.For example:-The string is he loves to play cricket and the given task is sortword 2.Then the output would be "cricket he to play loves" only the first two words are sorted rest remainsunsorted 

Xaviers friend plans to write a program to solve these questions easily.

Input FORMAT

The first line inputs the String on which the task is to be performed.
Next line denotes number of test cases T.
The next line inputs the T NUMBER tasks to be performed one by one.

Output Format

The output string after the application of each function one by one.

SAMPLE INPUT
my name is xavier
2
Wordrev 3
sortword 2

SAMPLE OUTPUT
ym eman si xavier
is my name xavier
"""

def perform_string_operations(original_string, num_tasks, tasks):
    """
    Perform various string operations based on the given tasks.

    Parameters:
    - original_string (str): The original string on which the tasks are to be performed.
    - num_tasks (int): The number of tasks to be performed.
    - tasks (list of tuples): A list of tasks, where each task is a tuple (command, index).

    Returns:
    - list of str: A list of results, where each result corresponds to the output of each task.
    """
    
    def sort_words(seq, n):
        res = []
        for x in range(n):
            cur = min(seq)
            seq.remove(cur)
            res.append(cur)
        for x in seq:
            res.append(x)
        return res
    
    results = []
    s = original_string.strip().split()
    
    for task in tasks:
        com, ndx = task
        ndx = int(ndx)
        res = []
        
        if com == "Wordrev":
            for i in range(ndx):
                res.append(s[i][::-1])
            for i in range(ndx, len(s)):
                res.append(s[i])
            results.append(" ".join(res))
        
        elif com == "subpalin":
            count = 0
            q = ""
            for c in s:
                q += str(c) + " "
            l = len(q)
            for i in range(l):
                for j in range(i + 2, l):
                    if q[i:j] == q[i:j][::-1]:
                        count += 1
                    if count == ndx:
                        results.append(q[i:j])
                        break
                if count == ndx:
                    break
        
        elif com == "sortword":
            res = sort_words(s, ndx)
            results.append(" ".join(res))
    
    return results