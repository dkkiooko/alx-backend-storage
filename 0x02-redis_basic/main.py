#!/usr/bin/env python3
"""main file"""

import redis


Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data = data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))