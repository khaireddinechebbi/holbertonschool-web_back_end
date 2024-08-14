#!/usr/bin/env python3
"""
This script takes a list of integers and floats and retuns their sum as float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing both integers and floats.

    Parameters:
    mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Returns:
    float: The sum of all the numbers in the list as a float.
    """
    return sum(mxd_lst)
