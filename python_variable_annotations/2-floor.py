#!/usr/bin/env python3
"""
This script defines a function that returns the floor of a float.
"""


def floor(n: float) -> int:
    """
    Returns the floor of a float.

    Parameters:
    n (float): The float value to floor.

    Returns:
    int: The largest integer less than or equal to the given float.
    """
    return int(n // 1)
