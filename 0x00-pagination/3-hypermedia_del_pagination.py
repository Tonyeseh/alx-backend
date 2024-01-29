#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


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
        """Returns a dictionary with the following keys and values:
            index: the current start index of the return page
            next_index: the next index to query with the returned
            page_size: the current page size of the return page
            data: the actual page of the dataset
        """
        start_idx = idx = 0 if index is None else index
        dataset = self.indexed_dataset()
        len_dataset = len(self.indexed_dataset())
        assert start_idx < len_dataset
        next_idx = start_idx + page_size
        data = []

        for _ in range(page_size):
            while (not dataset.get(idx)):
                idx += 1
            data.append(dataset.get(idx))
            idx += 1

        return {
            "index": start_idx,
            "next_index": idx,
            "page_size": len(data),
            "data": data
        }
