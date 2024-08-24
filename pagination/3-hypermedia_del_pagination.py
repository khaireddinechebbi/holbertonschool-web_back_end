#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
            """
        Returns a dictionary containing pagination information including a resilient index system.

        Args:
            index (int): The current start index of the return page.
            page_size (int): The number of items per page.

        Returns:
            Dict[str, Any]: A dictionary with the pagination information.
        """
        assert isinstance(index, int) and 0 <= index < len(self.indexed_dataset())

        dataset = self.indexed_dataset()
        data = []
        current_index = index
        remaining_items = page_size

        while remaining_items > 0 and current_index < len(dataset):
            if current_index in dataset:
                data.append(dataset[current_index])
                remaining_items -= 1
            current_index += 1

        next_index = current_index if current_index < len(dataset) else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }

