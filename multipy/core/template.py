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
    .
    .
    .
]

The "run" of a given element determines where adders, run=2, or a
combination of CSAs and HAs, run=3, are used. Elements can be
int or strings, as long as they follow the "run" principle.

Complex templates require a more rigorous approach.

"""
from typing import Any
import multipy as mp

class Template:
    def __init__(self, pattern: list[Any]): # Complex or simple
        self.pattern = pattern
        valid_range = mp.SUPPORTED_BIT_LENGTHS
        if len(pattern) not in valid_range:
            raise ValueError(f"Valid bit lengths: {valid_range}")
        self.bits = len(pattern)


    def __build_template(self) -> list[list[int]]:
        """
        Build a logic AND matrix for a bitwidth of self.bits. For example:
        >>> self.bits = 4
        >>> build_matrix()
        [['_','_','_','_',0,0,0,0],
         ['_','_','_',0,0,0,0,'_'],
         ['_','_',0,0,0,0,'_','_'],
         ['_',0,0,0,0,'_','_','_']]
        """
        row = [0]*self.bits
        matrix = []
        for i in range(self.bits):
            matrix.append(["_"]*(self.bits-i) + row + ["_"]*i)
        return matrix







"""
Complex templates implement decoders and bit-mapping.

Decoders reduce 4 or more bits at a time.

Bit mapping allows for outlining where bits are placed in each stage,
enabling complex implementations and possible optimisations.
"""
