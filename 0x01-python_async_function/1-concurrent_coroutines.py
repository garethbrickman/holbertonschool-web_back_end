#!/usr/bin/env python3
""" Takes 2 int args, waits for random delay """

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(max_delay: int = 10, n: int) -> List[float]:
    """ Waits for ran delay until max_delay, returns list of actual delays """
    pass
