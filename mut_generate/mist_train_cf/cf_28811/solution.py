"""
QUESTION:
Implement the `get_rds_digests` function to calculate and return a list of digests for a given list of documents. If the digests are already present in the cache, retrieve them directly; otherwise, calculate the digests, store them in the cache, and return the result. The function should take two parameters: `documents` (a list of documents) and `cache` (a cache object with `get` and `set` methods). Assume that a separate `calculate_digest` function is available to calculate the digest of a single document.
"""

def get_rds_digests(documents, cache):
    try:
        rd_digests_cached = cache.get('rd_digests')
        if rd_digests_cached:
            return rd_digests_cached
        else:
            # Calculate digests for the documents
            digests = [calculate_digest(doc) for doc in documents]
            # Store the digests in the cache
            cache.set('rd_digests', digests)
            return digests
    except Exception as e:
        return f"Error: {e}"