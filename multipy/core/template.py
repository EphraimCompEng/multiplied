################################################
# Returns Template Objects Using User Patterns #
################################################



"""
Simple templates should be represented as a list with each element on
a new line, this makes it clear how each layer is reduced:
>>> my_simple_template = [
    1,
    1,
    2,
    2,
    2,
    ...
]

The "run" of a given element determines where adders, run=2, or a
combination of CSAs and HAs, run=3, are used.
"""
