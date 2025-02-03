from copy import deepcopy
from NumericalMethods import GaussSeidel

def main():
    #equation set 1
    Aaug1 = [
    [4, -1, 0, 3],
    [-1, 4, -1, 3],
    [0, -1, 4, 3]
    ]
    x1 = [0, 0, 0]
    solution1 = GaussSeidel(Aaug1, x1, Niter = 15)
    print("Solution to the first set of equations: {}".format(solution1))
    #equation set 2
    Aaug2 = [
    [3, -0.1, -0.2, 7.85],
    [0.1, 7, -0.3, -19.3],
    [0.3, -0.2, 10, 71.4]
    ]
    x2 = [0, 0, 0]
    solution2 = GaussSeidel(Aaug2, x2, Niter = 15)
    print("Solution to the second set of equations: {}".format(solution2))

if __name__=="__main":
    main()

    #Could not get an output for this code :(