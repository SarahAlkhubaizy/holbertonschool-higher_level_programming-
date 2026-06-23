#!/usr/bin/env python3
"""Module for CountedIterator class."""


class CountedIterator:
    """Iterator that counts the number of items fetched."""

    def __init__(self, iterable):
        """Initialize with an iterable and a counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Return the number of items iterated."""
        return self.count

    def __next__(self):
        """Fetch next item and increment counter."""
        item = next(self.iterator)
        self.count += 1
        return item

    def __iter__(self):
        """Return self as iterator."""
        return self
