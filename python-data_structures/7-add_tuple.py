#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elements by adding (0, 0) to them
    # and then slicing the first 2 elements.
    a = (tuple_a + (0, 0))[:2]
    b = (tuple_b + (0, 0))[:2]
    
    # Return a new tuple with the sums of the corresponding elements
    return (a[0] + b[0], a[1] + b[1])
