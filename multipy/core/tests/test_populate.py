################################
# Import Modules Without Error #
################################

import multipy as mp

def test_empty_matrix():
    matrix = mp.MpMatrix(8)
    print(matrix)
    assert matrix.matrix == [
        ['_', '_', '_', '_', '_', '_', '_', '_', 0, 0, 0, 0, 0, 0, 0, 0],
        ['_', '_', '_', '_', '_', '_', '_', 0, 0, 0, 0, 0, 0, 0, 0, '_'],
        ['_', '_', '_', '_', '_', '_', 0, 0, 0, 0, 0, 0, 0, 0, '_', '_'],
        ['_', '_', '_', '_', '_', 0, 0, 0, 0, 0, 0, 0, 0, '_', '_', '_'],
        ['_', '_', '_', '_', 0, 0, 0, 0, 0, 0, 0, 0, '_', '_', '_', '_'],
        ['_', '_', '_', 0, 0, 0, 0, 0, 0, 0, 0, '_', '_', '_', '_', '_'],
        ['_', '_', 0, 0, 0, 0, 0, 0, 0, 0, '_', '_', '_', '_', '_', '_'],
        ['_', 0, 0, 0, 0, 0, 0, 0, 0, '_', '_', '_', '_', '_', '_', '_']
    ]

def test_build_matrix():
    matrix = mp.MpMatrix(8)
    matrix.build_matrix(15, 15)
    print(matrix)
    # assert matrix.matrix

    # assert matrix.matrix ==

def main() -> None:
    test_empty_matrix()
    test_build_matrix()
    temp1 = mp.MpMatrix(8)
    print(temp1.bits)
    temp2 = mp.MpMatrix(8)
    print(temp2.bits)
    alg = mp.Algorithm()
    arg = [temp1, temp2]
    alg.populate(arg)

    print(alg)
    print(alg.bits)

if __name__ == "__main__":
    main()
