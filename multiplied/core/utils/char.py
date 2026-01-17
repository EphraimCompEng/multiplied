from collections.abc import Generator


# --  Character related helper functions ----------------------------

def ischar(ch:str) -> bool:
    """
    Tests if a string is exactly one alphabetic character
    """
    try:
        ord(ch)
        return True
    except (ValueError, TypeError):
        return False

def chargen() -> Generator[str]:
    i = 0
    while True:
        yield chr((i % 26) + 65)
        i += 1




# -- testing --------------------------------------------------------
def main():
    test = chargen()
    for _ in range(32):
        print(next(test))

if __name__ == "__main__":
    main()
