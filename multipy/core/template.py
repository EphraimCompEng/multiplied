################################################
# Returns Template Objects Using User Patterns #
################################################

from typing import Any
import multipy as mp
import copy



def _is_char(ch:str) -> bool:
    """
    Tests if a string is exactly one alphabetic character
    """
    try:
        ord(ch)
        return True
    except (ValueError, TypeError):
        return False


def build_simple_template(pattern: list[str]
) -> list[list[str]]:
    """
    Build a simple template for a given bitwidth.
    >>> self.bits = 4
    >>> build_template(self.pattern)
    [['_','_','_','_','a','a','a','a'], # p = ['a',
        ['_','_','_','a','a','a','a','_'], #      'a',
        ['_','_','b','b','b','b','_','_'], #      'b',
        ['_','b','b','b','b','_','_','_']] #      'b',]
    """
    matrix = []

    return matrix

# Defining a new Template type for list[list[Any]] would be useful?

def build_csa(
    char: str, template_slice: list[list[Any]]
) -> tuple[list, list]: # Carry Save Adder -> (template, result)
    """
    Returns template "slices" for a csa reduction and the resulting slice.\n
    [slice]\t[csa]\t\t[result]\n
    ____0000 ____AaAa         \n
    ___0000_ ___aAaA_ __AaAaAa\n
    __0000__ __AaAa__ __aAaA__\n
    """
    if len(template_slice) != 3:
        raise ValueError("Invalid template slice: must be 3 rows")

    # loop setup
    n = len(template_slice[0])
    result = [['_']*n, ['_']*n]
    csa_slice = copy.copy(template_slice)
    tff = char == char.lower() # Toggle flip flop
    for i in range(n):
        # For int in template slice, map possible CSA operands to adder_slice
        # Then map possible outputs to result
        # [ bA + bB + bC = 0b00, 0b01, 0b10 ]
        # CSA auto maps Cout: FF, see templates/map.py
        csa_slice[0][i] = char if (y0:=csa_slice[0][i] != '_') else '_'
        csa_slice[1][i] = char if (y1:=csa_slice[1][i] != '_') else '_'
        csa_slice[2][i] = char if (y2:=csa_slice[2][i] != '_') else '_'
        result[0][i]    = char if 1 <= (y0+y1+y2) else '_'
        result[1][i-1]  = char if 1 < (y0+y1+y2) else '_'
        tff  = not(tff) # True -> False -> True...
        char = char.lower() if tff else char.upper()
    return csa_slice, result


def build_adder(
    char: str, template_slice: list[list[Any]]
) -> tuple[list, list]: # Carry Save Adder -> (template, result)
    """
    Returns template "slices" for addition and the resulting slice.\n
    [slice ]\t[adder]\t[result]\n
    ___0000_ ___aAaA_\n
    __0000__ __AaAa__ _aAaAaA_\n
    """
    if len(template_slice) != 2:
        raise ValueError("Invalid template slice: must be 2 rows")

    # loop setup
    n = len(template_slice[0])
    result = [['_']*n]
    adder_slice = copy.copy(template_slice) # ensure no references
    tff         = char == char.lower() # Toggle flip flop
    for i in range(n):
        # For int in template slice, map possible ADD operands to adder_slice
        # Then map possible outputs to result
        # [ bA + bB = 0b00, 0b01, 0b10, 0b11]
        adder_slice[0][i] = char if (y0:=adder_slice[0][i] != '_') else '_'
        adder_slice[1][i] = char if (y1:=adder_slice[1][i] != '_') else '_'
        result[0][i]      = char if y0 or y1 else '_'
        tff  = not(tff) # True -> False -> True...
        char = char.lower() if tff else char.upper()

    # Adding final carry
    tff      = not(tff) # Undo last flip to find last used tff value
    pre_char = char
    char     = char.lower() if tff else char.upper()
    index    = result[0].index(char)-1 # find first instance of char - 1
    result[0][index] = pre_char # Final carry place in result template

    return adder_slice, result

###
# Simple maps move entire rows
###

# def build_map(char: str, matrix: list[list[Any]]
# ) -> list[list[int]]:
#     """
#     A map matrix holds signed hexadecimal numbers representing a vertical
#     offset for a given bit when applied to an algorithm.

#     [map]\t   [matrix]\t[effect]\n
#     00 02 01\t _ 0 1\t  _ 1 _\n
#     00 FF 00\t 0 1 _\t  0 _ 1\n
#     00 00 00\t _ _ _\t  _ 0 _\n
#     """


#     ...


class Template:
    # import string
    # cell = (ch for ch in string.ascii_lowercase)

    def __init__(self, template: list[Any], result: Any = None): # Complex or simple
        valid_range  = mp.SUPPORTED_BITWIDTHS
        self.len     = len(template)
        self.result  = result
        self.pattern = None

        # length of any template represents it's bitwidth
        if len(template) not in valid_range:
            raise ValueError(f"Valid bit lengths: {valid_range}")
        if _is_char(template[0]):
            self.pattern  = template
            self.template, self.result  = build_simple_template(template)
        elif _is_char(template[0][0]):
            self.template = template








"""
Complex templates implement decoders and bit-mapping.

Decoders reduce 4 or more bits at a time.

Bit mapping allows for outlining where bits are placed in each stage,
enabling complex implementations and possible optimisations.
"""
