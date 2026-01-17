import multiplied as mp

def test_dadda_map(bits) -> None:
    try:
        mp.build_dadda_map(0)
    except AssertionError:
        pass
    m = mp.build_dadda_map(bits)
    mp.mprint(m)

def test_simple_map() -> None:
    sm = mp.Map(
        [
            '00',
            'FF',
            'FF',
            'FF',
        ]
    )
    mp.mprint(sm)
    m1 = mp.build_matrix(5, 5, 4)
    mp.mprint(m1)
    m1map = mp.resolve_rmap(m1)
    mp.mprint(m1map)




def main():

    test_dadda_map(8)




if __name__ == "__main__":
    main()
