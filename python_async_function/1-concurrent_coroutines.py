#!/usr/bin/env python3
"""
The wait_n function is an asynchronous coroutine designed to execute \
multiple instances of the wait_random coroutine concurrently. It takes\
two integer arguments: n and max_delay. The function spawns n instances \
of wait_random, each with a maximum delay of max_delay seconds, and \
collects the resulting delays into a list. The list is then returned \
in ascending order.
"""
import asyncio
from typing import List
from 0-basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random.

    Returns:
        List[float]: A list of all the delays (in ascending order).
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    
    return sorted(delays)

# Example usage:
if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
