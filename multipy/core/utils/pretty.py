from typing import Any
import multipy as mp


def pretty(matrix: Any) -> str:
    """
    Format matrix as a string:

    >>> ____0000
    >>> ___0000_
    >>> __0000__
    >>> _0000___
    """
    assert isinstance(matrix, (mp.Matrix, mp.Slice, list)), (
        "Unsupported type"
    )
    pretty_ = ""
    for i in matrix:
        row = [str(x) for x in i]
        pretty_ += "".join(row) + "\n"
    return pretty_



def pprint(matrix: Any):
    """Print formatted Matrix object"""
    pretty_ = pretty(matrix)
    print(pretty_)
