#!/usr/bin/env python3
"""
This scripts takes a string k and an int OR float v as arguments \
and returns a tuple. The first element of the tuple is the string k. \
The second element is the square of the int/float v and should be \
annotated as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is the string k \
    and the second element is the square of v.

    Parameters:
    k (str): The string key.
    v (Union[int, float]): The value which is either an \
    int or a float.

    Returns:
    Tuple[str, float]: A tuple containing the string k \
    and the square of v as a float.
    """
    retun(k, float(v**2))
