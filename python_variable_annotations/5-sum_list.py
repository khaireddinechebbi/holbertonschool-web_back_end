#!/usr/bin/env python3
"""
This script take a list of floats and retun thier sum
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Parameters:
    input_list (List[float]): A list of float values.

    Returns:
    float: The sum of all the floats in the list.
    """
    return sum(input_list)
