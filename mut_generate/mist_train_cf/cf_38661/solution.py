"""
QUESTION:
Implement the method `update_cache` that takes three parameters: `self`, `i`, and `content_label`. The method should update the RSU cache `content_label_R` at index `i` based on the requested `content_label`. If the `content_label` is already in the cache, move it to the front of the cache. If the `content_label` is not in the cache, shift existing content labels to make space for the new content and add it to the front of the cache. The method should return the updated cache state. The cache has a fixed size and the `content_label_R` is a 2D list where each sub-list represents a cache.
"""

def update_cache(self, i, content_label):
    if content_label in self.content_label_R[i]:  
        content_label_index = self.content_label_R[i].index(content_label)
        if content_label_index != 0:
            for j in range(content_label_index):
                self.content_label_R[i][j + 1] = self.content_label_R[i][j]
            self.content_label_R[i][0] = content_label
    else:  
        for j in range((self.max_cacheR // self.content_size) - 1, 0, -1):
            self.content_label_R[i][j] = self.content_label_R[i][j - 1]
        self.content_label_R[i][0] = content_label
    return self.content_label_R