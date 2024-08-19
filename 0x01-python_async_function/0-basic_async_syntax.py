#!/usr/bin/env python3
""" an asynchronous coroutine """


import asyncio
import random


async def wait_random(max_delay=10):
    """ an asynchronous coroutine
    ARGS:
        max_deley: int
    Return:
        the r the random number bettewn 0 and max_deley
    """

    r = random.uniform(0, max_delay)
    await asyncio.sleep(r)
    return r
