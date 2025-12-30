#############################################
# Returns Algorithm Objects Using Templates #
#############################################
"""
An algorithm is the application of multiple templates until no partial
products are left.

Algorithm objects must collect any number of templates based on:
    - bitwidth
    - template composition -- MultiPy should not stop users making any
      algorithm, even if suboptimal
    - Saturation -- Set to original bit width
    (Unsure if users likely to need saturation to arbitrary bitwidths)

Applying simple templates can be hardcoded, however complex templates
need to be analysed before execution. Especially so when implementing
decoders, flooding and sneaky tricks like using carry-in(cin) on adders.


"""


from typing import Any
from .matrix import MpMatrix

class Algorithm(MpMatrix):

    algorithm = {}
    def __init__(self) -> None:
        self.algorithm = {}
        self.bits = 0
        self.stages = len(self.algorithm)

    def populate(self, arg: Any) -> None:
        """
        Adds template(s) to an existing algorithm. All templates must be of
        consistent bitwidth.
        """

        if isinstance(arg, MpMatrix): # warp matrix in list to reuse code
            arg = [arg] # list(arg) throw error -- implement __iter___?
        elif not(isinstance(arg, list)):
            raise TypeError("Invalid argument type. Expected list[Matrix] or Matrix.")

        size = arg[0].bits if self.bits == 0 else self.bits
        for template in arg:
            if template.bits != size:
                raise ValueError("All templates must have consistent bitwidth.")
            self.algorithm[len(self.algorithm)] = template
        self.bits = size

    def __repr__(self) -> str:
        pretty = ""
        print()
        for i, t in self.algorithm.items():
            pretty += f"S{i}:\n" + self.pprint_matrix(t) + "\n"
        return pretty

    def step(self, matrix: MpMatrix) -> None:
        """
        Take youngest template, apply to matrix, remove template
        """
        ...
