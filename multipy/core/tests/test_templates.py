import multipy as mp



def test_build_csa4() -> None:
    matrix4  = mp.Matrix(4)
    pattern  = mp.Matrix(4)
    pattern = list(pattern.matrix[:3])
    print(matrix4.matrix)
    print(pattern)
    my_pattern = mp.Template.build_csa('a', pattern)
    print(mp.Matrix.pretty(matrix4.matrix))
    print(mp.Matrix.pretty(my_pattern[0]))
    print(mp.Matrix.pretty(my_pattern[1]))

def test_build_csa8() -> None:
    matrix8  = mp.Matrix(8)
    print(matrix8.matrix)
    pattern2  = mp.Matrix(8)
    pattern2 = list(pattern2.matrix[3:6])
    my_pattern = mp.Template.build_csa('b', pattern2)
    print(mp.Matrix.pretty(matrix8.matrix))
    print(mp.Matrix.pretty(my_pattern[0]))
    print(mp.Matrix.pretty(my_pattern[1]))

    # print(pattern)
    # print(mp.Matrix.pretty(my_matrix.matrix))
    # my_pattern = mp.Template.build_csa('a', pattern)
    # print(mp.Matrix.pretty(my_matrix.matrix))
    # print(mp.Matrix.pretty(my_pattern[0]))
    # print(mp.Matrix.pretty(my_pattern[1]))



def main() -> None:
    test_build_csa4()
    test_build_csa8()

if __name__ == "__main__":
    main()
