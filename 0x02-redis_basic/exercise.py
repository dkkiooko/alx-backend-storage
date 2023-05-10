#!/usr/bin/env python3
"""writing strings to redis"""
import uuid
import redis
from functools import wraps
from typing import Callable, Union


def count_calls(method: Callable) -> Callable:
    """ counts number of times a method is called """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ wrapper function """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

class Cache:
    """ Cache class"""
    def __init__(self) -> None:
        """initialize the cache"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store data in cache """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Callable = None
            ) -> Union[str, bytes, int, float]:
        """ retrieve value from redis data storage """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """ get a string from the cache """
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        """ get an int from the cache """
        value = self._redis.get(key)
        return int(value)
