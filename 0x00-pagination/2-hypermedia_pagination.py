#!/usr/bin/env python3
"""2-hypermedia_pagination"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns the tuple of size  two containing a start index
    and an end index corresponding to the range of indexes to
    return in a list for those particular pagination parameters."""

    return (page - 1) * page_size, page * page_size


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
        """gets the correct indexes to paginate the dataset
        and return the appropriate page of the dataset"""
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page_size > 0
        assert page > 0

        start_idx, end_idx = index_range(page, page_size)
        return self.dataset()[start_idx: end_idx]

    def get_hyper(self, page: int, page_size: int):
        """returns a dictionary contain the following key-value pairs
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        int_page = len(self.dataset()) // page_size
        rem_page = len(self.dataset()) % page_size
        data = self.get_page(page, page_size)
        data_size = len(data)
        total_pages = int_page if rem_page == 0 else int_page + 1
        next_page = None if page == total_pages else page + 1
        prev_page = None if page == 1 else page - 1

        return {
            "page_size": data_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
