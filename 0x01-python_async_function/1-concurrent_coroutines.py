#!/usr/bin/env python3
"""spawn wait_random n times with the specified max_delay"""


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """return the list of all the delays (float values). The list of the
    delaysshould be in ascending order without using sort()
    because of concurrency."""
    res = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    complated = asyncio.as_completed(tasks)
    for task in complated:
        t = await task
        res.append(t)
    return res
