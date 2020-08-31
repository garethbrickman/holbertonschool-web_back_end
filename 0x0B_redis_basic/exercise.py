#!/usr/bin/env python3
""" Module for Redis db """
from uuid import uuid4

from typing import Union


class Cache:
    """ Placeholder text """

    def __init__(self):
        """ Placeholder text """
        #_redis = instanceOfRedisClient
        # #flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Placeholder text """
        key = uuid4()
        #store input data in Redis using key
        return key
