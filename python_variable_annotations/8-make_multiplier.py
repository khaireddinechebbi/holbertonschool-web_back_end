#!/usr/bin/env python3
"""
This script takes a float multiplier as argument and returns a function that\
 multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Parameters:
    multiplier (float): The multiplier to apply.

    Returns:
    Callable[[float], float]: A function that takes a float\
     and returns it multiplied by the multiplier.
    """
    def multiplier_function(x: float) -> float:
        """
        Returns float multiplied by a given multiplier.

        Parameters:
        x (float): float

        Returns:
        float
        """
        return x * multiplier

    return multiplier_function
