"""
QUESTION:
Implement the `process_data(images, questions, answers)` function that takes three batches as input: 
- `images`: a 4D tensor with dimensions [batch_size, height, width, channels] representing a batch of images.
- `questions`: a 2D tensor with dimensions [batch_size, max_question_length] representing a batch of questions.
- `answers`: a 1D tensor with dimensions [batch_size] representing a batch of answers.

The function should perform the following operations and return the results:
- Calculate the average pixel intensity for each image in the batch and store it in a list.
- Concatenate each question with its corresponding answer and store it in a list.

The function should return a tuple of two lists: the first list contains the average pixel intensities, and the second list contains the concatenated question-answer pairs.

The function signature should be `def process_data(images, questions, answers) -> Tuple[List[float], List[str]]`.
"""

from typing import List, Tuple
import numpy as np

def process_data(images, questions, answers) -> Tuple[List[float], List[str]]:
    avg_pixel_intensities = [np.mean(image) for image in images]
    concatenated_qa_pairs = [str(question) + str(answer) for question, answer in zip(questions, answers)]
    return avg_pixel_intensities, concatenated_qa_pairs