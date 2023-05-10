#!/usr/bin/env python3
"""writing strings to redis"""
import uuid
import redis
from typing import Union

class Cache:
    """ Cache class"""
    def __init__(self) -> None:
        """initialize the cache"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store data in cache """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
