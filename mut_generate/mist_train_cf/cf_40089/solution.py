"""
QUESTION:
Implement an `AsyncCache` class with a maximum size `max_size` that provides asynchronous caching functionality for coroutines. The class should have two methods: `cache(key: str, coro: Callable[..., Any])` to asynchronously cache the result of `coro` with the specified `key`, and `get(key: str)` to asynchronously retrieve the cached result associated with `key`. The cache should handle concurrent access in a thread-safe manner and remove the oldest item when full.
"""

import asyncio
from typing import Any, Callable
from collections import OrderedDict

def AsyncCache(max_size: int):
    cache = OrderedDict()
    lock = asyncio.Lock()

    async def cache(key: str, coro: Callable[..., Any]) -> Any:
        """Asynchronously cache the result of coro with the specified key."""
        async with lock:
            if key in cache:
                return cache[key]
            result = await coro()
            if len(cache) >= max_size:
                cache.popitem(last=False)  # Remove the oldest item when the cache is full
            cache[key] = result
            return result

    async def get(key: str) -> Any:
        """Asynchronously retrieve the cached result associated with key."""
        async with lock:
            return cache.get(key)

    return cache, get