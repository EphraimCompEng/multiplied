import multiplied as mp

# -- testing --------------------------------------------------------
def main():
    testgen = mp.chargen()
    for _ in range(32):
        tmp = next(testgen)
        testtff = mp.chartff(tmp)
        for _ in range(8):
            print(next(testtff), end='')
        print(tmp)

if __name__ == "__main__":
    main()
