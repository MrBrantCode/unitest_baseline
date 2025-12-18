"""
QUESTION:
Write a function `nextBook(bookList, currentIndex)` that moves to the next book in the list and prints its name, author, and genre. The function should return a boolean value indicating whether there are more books to read after the current book.
"""

def nextBook(bookList, currentIndex):
    if currentIndex < len(bookList):
        currentBook = bookList[currentIndex]
        print("Book Name:", currentBook["name"])
        print("Author:", currentBook["author"])
        print("Genre:", currentBook["genre"])
        return currentIndex + 1 < len(bookList)
    else:
        print("End of List")
        return False