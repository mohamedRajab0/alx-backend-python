#!/usr/bin/env python3
"""measures the total execution time
for wait_n(n, max_delay), and returns total_time / n"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay):
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay)) 
    return time.perf_counter() - start_time
