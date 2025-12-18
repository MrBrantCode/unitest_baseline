"""
QUESTION:
Saying that it is not surprising that people want to know about their love, she has checked up his address, name, age, phone number, hometown, medical history, political party and even his sleeping position, every piece of his personal information. The word "privacy" is not in her dictionary. A person like her is called "stoker" or "yandere", but it doesn't mean much to her.

To know about him, she set up spyware to his PC. This spyware can record his mouse operations while he is browsing websites. After a while, she could successfully obtain the record from the spyware in absolute secrecy.

Well, we want you to write a program which extracts web pages he visited from the records.

All pages have the same size H × W where upper-left corner is (0, 0) and lower right corner is (W, H). A page includes several (or many) rectangular buttons (parallel to the page). Each button has a link to another page, and when a button is clicked the browser leads you to the corresponding page.

His browser manages history and the current page in the following way:

The browser has a buffer of 1-dimensional array with enough capacity to store pages, and a pointer to indicate a page in the buffer. A page indicated by the pointer is shown on the browser. At first, a predetermined page is stored and the pointer indicates that page. When the link button is clicked, all pages recorded in the right side from the pointer are removed from the buffer. Then, the page indicated by the link button is stored into the right-most position of the buffer, and the pointer moves to right. As a result, the user browse the page indicated by the button.

The browser also has special buttons 'back to the previous page' (back button) and 'forward to the next page' (forward button). When the user clicks the back button, the pointer moves to left, and the user clicks the forward button, the pointer moves to right. But in both cases, if there are no such pages in the buffer, nothing happen.

The record consists of the following operations:


click x y


It means to click (x, y). If there is a button on the point (x, y), he moved to the corresponding page. If there is nothing in the point, nothing happen. The button is clicked if x1 ≤ x ≤ x2 and y1 ≤ y ≤ y2 where x1, x2 means the leftmost and rightmost coordinate and y1, y2 means the topmost and bottommost coordinate of the corresponding button respectively.


back


It means to click the Back button.


forward


It means to click the Forward button.

In addition, there is a special operation show. Your program should print the name of current page for each show operation.

By the way, setting spyware into computers of others may conflict with the law. Do not attempt, or you will be reprimanded by great men.

Constraints

* 1 ≤ n ≤ 100
* b[i] ≤ 100
* 1 ≤ the number of characters in the name ≤ 20
* Buttons are not touch, overlapped nor run over from the browser.

Input

Input consists of several datasets.

Each dataset starts with an integer n which represents the number of pages in the dataset.

Next line contains two integers W and H.

Next, information of each page are given. Each page starts with a string of characters and b[i], the number of buttons the page has. Following b[i] lines give information of buttons. Each button consists of four integers representing the coordinate (x1, y1) of upper left corner and the coordinate (x2, y2) of lower right corner of the button and a string of characters, which represents the name of page that the link of the button represents.

Next, the number of operation m is given. Following m lines represent the record of operations. Please see the above description for the operation.

The first page is stored in the buffer at first.

Input ends when n = 0.

Output

For each dataset, output the name of current page for each show operation.

Example

Input

3
800 600
index 1
500 100 700 200 profile
profile 2
100 100 400 200 index
100 400 400 500 link
link 1
100 100 300 200 index
9
click 600 150
show
click 200 450
show
back
back
show
forward
show
0


Output

profile
link
index
profile
"""

def process_browser_history(n, W, H, pages, operations):
    # Dictionary to map page names to their indices
    page_dict = {page[0]: idx for idx, page in enumerate(pages)}
    
    # Buffer to store the history of pages
    buffer = [0] * 2000
    now, sz = 0, 1
    
    # Initialize the buffer with the first page
    buffer[now] = 0
    
    # List to store the results of show operations
    results = []
    
    for operation in operations:
        parts = operation.split()
        if parts[0] == 'back':
            if now > 0:
                now -= 1
        elif parts[0] == 'forward':
            if now < sz - 1:
                now += 1
        elif parts[0] == 'show':
            results.append(pages[buffer[now]][0])
        elif parts[0] == 'click':
            x, y = int(parts[1]), int(parts[2])
            current_page_buttons = pages[buffer[now]][1]
            for (x1, y1, x2, y2, link_name) in current_page_buttons:
                if x1 <= x <= x2 and y1 <= y <= y2:
                    now += 1
                    buffer[now] = page_dict[link_name]
                    sz = now + 1
                    break
    
    return results