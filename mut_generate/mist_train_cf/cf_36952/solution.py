"""
QUESTION:
Implement the function `update_requests(num_books, request_list)` where `num_books` is an integer representing the total number of books available and `request_list` is a list of integers representing the list of book requests. The function should return a tuple `(fulfilled_requests, remaining_requests)` where `fulfilled_requests` is a list of integers representing the status of fulfilled requests (1 if fulfilled, 0 if not) and `remaining_requests` is a list of integers representing the remaining requests after fulfillment. The function should handle the fulfillment of requests based on the available books and update the status of fulfilled requests and the remaining requests accurately.
"""

def entrance(num_books, request_list):
    fulfilled_requests = [0] * len(request_list)
    remaining_requests = request_list.copy()

    for i in range(len(request_list)):
        if num_books >= request_list[i]:
            fulfilled_requests[i] = 1
            remaining_requests[i] = 0
            num_books -= request_list[i]
        else:
            remaining_requests[i] -= num_books
            num_books = 0

    return fulfilled_requests, remaining_requests