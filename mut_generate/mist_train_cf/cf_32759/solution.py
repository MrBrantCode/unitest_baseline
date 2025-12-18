"""
QUESTION:
Implement the `process_queue` function, which takes a queue of JSON objects and a number of worker threads as input. The function should use a ThreadPoolExecutor to process the JSON objects concurrently. Each JSON object contains the fields "id" (a unique identifier for the task) and "data" (the data to be processed). The processing operation involves doubling the value of the "data" field and storing the result in a dictionary with the "id" as the key. If an exception occurs during processing, capture the error and include it in the results. The function should return the dictionary containing the processed results.
"""

import json
from concurrent.futures import ThreadPoolExecutor

def process_queue(task_queue, num_threads):
    results = {}
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        while not task_queue.empty():
            task = task_queue.get()
            try:
                result = executor.submit(lambda task: {"id": task["id"], "result": task["data"] * 2}, task).result()
                results[result["id"]] = result["result"]
            except Exception as e:
                results[task["id"]] = f"Error processing task: {str(e)}"
            finally:
                task_queue.task_done()
    return results