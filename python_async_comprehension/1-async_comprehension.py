#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine for collecting random numbers.

Functions:
    async_comprehension: Collects and returns 10 random numbers generated asynchronously.
"""

import asyncio
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator and returns them.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    return [num async for num in async_generator()]
