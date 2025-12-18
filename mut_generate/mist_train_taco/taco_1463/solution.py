"""
QUESTION:
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows: 

If the book is returned on or before the expected return date, no fine will be charged (i.e.: $fine=0)$.
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, $fine=15\ \text{Hackos}\ \times\ \text{(the number of days later)}$. 
If the book is returned after the expected return month but still within the same calendar year as the expected return date, the $fine=500\ \text{Hackos}\ \times\ \text{(the number of months rate)}$.   
If the book is returned after the calendar year in which it was expected, there is a fixed fine of $10000\ \textbf{Hackos}$.

Charges are based only on the least precise measure of lateness.  For example, whether a book is due January 1, 2017 or December 31, 2017, if it is returned January 1, 2018, that is a year late and the fine would be $10,000\ \text{Hackos}$.  

Example 

$d1,m1,y1=14,7,2018$ 

$d2,m2,y2=5,7,2018$  

The first values are the return date and the second are the due date.  The years are the same and the months are the same.  The book is $14-5=9$ days late.  Return $9*15=135$.  

Function Description  

Complete the libraryFine function in the editor below.  

libraryFine has the following parameter(s):  

d1, m1, y1: returned date day, month and year, each an integer  
d2, m2, y2: due date day, month and year, each an integer    

Returns  

int:  the amount of the fine or $\mbox{o}$ if there is none

Input Format

The first line contains $3$ space-separated integers, $d1,m1,y1$, denoting the respective $\boldsymbol{day}$, $\textit{month}$, and $year$ on which the book was returned. 

The second line contains $3$ space-separated integers, $d2,m2,y2$, denoting the respective $\boldsymbol{day}$, $\textit{month}$, and $year$ on which the book was due to be returned.

Constraints

$1\leq d1,d2\leq31$     
$1\leq m1,m2\leq12$     
$1\leq y1,y2\leq3000$  
$\textbf{It is generated that the dates will be valid Gregion calendar dates.}$  

Sample Input
9 6 2015
6 6 2015

Sample Output
45

Explanation

Given the following dates: 

Returned: $d1=9,m1=6,y1=2015$ 

Due: $d2=6,m2=6,y2=2015$

Because $y2\equiv y1$, we know it is less than a year late. 

Because $\textit{m2}\equiv\textit{m1}$, we know it's less than a month late. 

Because $d2<d1$, we know that it was returned late (but still within the same month and year).  

Per the library's fee structure, we know that our fine will be $15\ \text{Hackos}\ \times\ (\#\ \text{days rate})$. We then print the result of $15\times(d1-d2)=15\times(9-6)=45$ as our output.
"""

def calculate_library_fine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return 10000
    elif y1 == y2:
        if m1 > m2:
            return 500 * (m1 - m2)
        elif m1 == m2:
            if d1 > d2:
                return 15 * (d1 - d2)
    return 0