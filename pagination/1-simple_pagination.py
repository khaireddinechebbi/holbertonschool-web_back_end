#!/usr/bin/env python3
"""
Pagination module for managing popular baby names dataset.

This script provides a Server class to paginate a dataset loaded from
a CSV file.
The pagination is done using a helper function `index_range`, which calculates
the appropriate start and end indexes for a given page and page size.

Classes:
    Server: A class to paginate a dataset of popular baby names.

Functions:
    index_range(page: int, page_size: int) -> Tuple[int, int]:
        Calculate start and end index for pagination.

Usage Example:
    server = Server()
    page_data = server.get_page(1, 10)  # Gets the first 10 records.
"""
import csv
import math
from typing import List
index_range = __import__("0-simple_helper_function").index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the appropriate page of the dataset.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: The list of rows for the specified page.
        """
        assert isinstance(
            page, int) and page > 0,
        "page must be a positive integer"
        assert isinstance(
            page_size, int) and page_size > 0,
        "page_size must be a positive integer"
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]
