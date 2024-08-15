#!/usr/bin/env python3
"""
This module defines a function `element_length` that takes an iterable of \
sequences and returns a list of tuples.
Each tuple contains a sequence from the iterable and its length.
"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculates the length of each sequence in the provided iterable.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences\
        (e.g., strings, lists, tuples).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains\
        a sequence from the input iterable and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
