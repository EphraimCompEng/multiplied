
# Work towards a more elegant solution to testing #

import multipy as mp



def test_temp_build_csa4() -> None:
    matrix4  = mp.Matrix(4)
    pattern  = mp.Matrix(4)
    pattern = list(pattern.matrix[:3])
    my_pattern = mp.Template.build_csa('a', pattern)
    print(mp.Matrix.pretty(matrix4.matrix))
    print(mp.Matrix.pretty(my_pattern[0]))
    print(mp.Matrix.pretty(my_pattern[1]))

def test_temp_build_csa8() -> None:
    matrix8  = mp.Matrix(8)
    pattern2  = mp.Matrix(8)
    pattern2 = list(pattern2.matrix[3:6])
    my_pattern = mp.Template.build_csa('b', pattern2)
    print(mp.Matrix.pretty(matrix8.matrix))
    print(mp.Matrix.pretty(my_pattern[0]))
    print(mp.Matrix.pretty(my_pattern[1]))

def test_temp_build_adder4() -> None:
    matrix4 = mp.Matrix(4)
    pattern = mp.Matrix(4)
    pattern = list(pattern.matrix[2:])
    my_pattern = mp.Template.build_adder('a', pattern)
    print(mp.Matrix.pretty(matrix4.matrix))
    print(mp.Matrix.pretty(my_pattern[0]))
    print(mp.Matrix.pretty(my_pattern[1]))

def test_temp_build_adder8() -> None:
    matrix4 = mp.Matrix(8)
    pattern = mp.Matrix(8)
    pattern = list(pattern.matrix[:2])
    my_pattern = mp.Template.build_adder('a', pattern)
    print(mp.Matrix.pretty(matrix4.matrix))
    print(mp.Matrix.pretty(my_pattern[0]))
    print(mp.Matrix.pretty(my_pattern[1]))

def main() -> None:
    test_temp_build_csa4()
    test_temp_build_csa8()
    test_temp_build_adder4()
    test_temp_build_adder8()

if __name__ == "__main__":
    main()
