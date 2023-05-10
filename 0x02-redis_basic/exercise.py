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


def call_history(method: Callable) -> Callable:
    """ store history of inputs and outputs for a function """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ return method's output after sorting inputs and outputs """
        in_key = '{}:inputs'.format(method.__qualname__)
        out_key = '{}:outputs'.format(method.__qualname__)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(in_key, str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(out_key, output)
        return output
    return wrapper


def replay(method: Callable) -> None:
    """ replays entire history of a function """
    name = method.__qualname__
    cache = redis.Redis()
    calls = cache.get(name).decode("utf-8")
    print("{} was called {} times:".format(name, calls))
    inputs = cache.lrange(name + ":inputs", 0, -1)
    outputs = cache.lrange(name + ":outputs", 0, -1)
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".
              format(name, i.decode('utf-8'), o.decode('utf-8')))


class Cache:
    """ Cache class"""
    def __init__(self) -> None:
        """initialize the cache"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @count_calls
    @call_history
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
