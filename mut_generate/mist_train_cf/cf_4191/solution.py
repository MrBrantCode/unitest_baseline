"""
QUESTION:
Create a function `categorize_dataset` that takes a list of positive integers as input and returns four lists, each representing a class with an equal number of elements and a sum as close to equal as possible. The function should aim to minimize the difference between the maximum and minimum sum of elements in each class. The input list must have a length that is a multiple of 4.
"""

def categorize_dataset(dataset):
    dataset.sort(reverse=True)
    total_sum = sum(dataset)
    target_sum = total_sum / 4
    classes = [[] for _ in range(4)]
    class_sums = [0] * 4

    for element in dataset:
        min_class_idx = class_sums.index(min(class_sums))
        classes[min_class_idx].append(element)
        class_sums[min_class_idx] += element

    diff = max(class_sums) - min(class_sums)
    if diff == 0:
        return classes

    for i in range(4):
        for j in range(i + 1, 4):
            if class_sums[i] > class_sums[j]:
                max_class_idx = i
                min_class_idx = j
            else:
                max_class_idx = j
                min_class_idx = i

            for element in classes[max_class_idx]:
                if class_sums[max_class_idx] - element < target_sum:
                    continue
                if class_sums[min_class_idx] + element > target_sum:
                    continue
                new_diff = max(class_sums[:max_class_idx] + [class_sums[max_class_idx] - element] +
                              class_sums[max_class_idx + 1:min_class_idx] +
                              [class_sums[min_class_idx] + element] + class_sums[min_class_idx + 1:]) - \
                           min(class_sums[:max_class_idx] + [class_sums[max_class_idx] - element] +
                              class_sums[max_class_idx + 1:min_class_idx] +
                              [class_sums[min_class_idx] + element] + class_sums[min_class_idx + 1:])
                if new_diff < diff:
                    class_sums[max_class_idx] -= element
                    class_sums[min_class_idx] += element
                    classes[max_class_idx].remove(element)
                    classes[min_class_idx].append(element)
                    diff = new_diff
                else:
                    continue

    return classes