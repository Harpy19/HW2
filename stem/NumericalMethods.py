#region imports
import Gauss_Elim as GE  # this is the module from lecture 2 that has useful matrix manipulation functions
from math import sqrt, pi, exp, cos
#endregion
                                            #majority of this code is from copilot
#region function definitions
def Probability(PDF, args, c, GT=True):
    """
    This is the function to calculate the probability that x is >c or <c depending
    on the GT boolean.
    Step 1:  unpack args into mu and stDev
    Step 2:  compute lhl and rhl for Simpson
    Step 3:  package new tuple args1=(mu, stDev, lhl, rhl) to be passed to Simpson
    Step 4:  call Simpson with GNPDF and args1
    Step 5:  return probability
    :param PDF: the probability density function to be integrated
    :param args: a tuple with (mean, standard deviation)
    :param c: value for which we ask the probability question
    :param GT: boolean deciding if we want probability x>c (True) or x<c (False)
    :return: probability value
    """
    mu, sig = args
    lhl = mu - 5 * sig
    rhl = c
    if GT:
        return 1 - Simpson(PDF, (mu, sig, lhl, rhl))
    else:
        return Simpson(PDF, (mu, sig, lhl, rhl))

def GPDF(args):
    """
    Here is where I will define the Gaussian probability density function.
    This requires knowing the population mean and standard deviation.
    To compute the GPDF at any value of x, I just need to compute as stated
    in the homework assignment.
    Step 1:  unpack the args tuple into variables called: x, mu, stDev
    Step 2:  compute GPDF value at x
    Step 3:  return value
    :param args: (x, mean, standard deviation)  tuple in that order
    :return: value of GPDF at the desired x
    """
    # Step 1: unpack args
    x, mu, sig = args
    # step 2: compute GPDF at x
    fx = (1 / (sig * sqrt(2 * pi))) * exp(-0.5 * ((x - mu) / sig) ** 2)
    # step 3: return value
    return fx

def Simpson(fn, args, N=100):
    """
    This executes the Simpson 1/3 rule for numerical integration (see page 832, Table 19.4).
    As I recall:
    1. divide the range from x=lhl to x=rhl into an even number of parts. Perhaps 20?
    2. compute fx at each x value between lhl and rhl
    3. sum the even and odd values of fx as prescribed
    4. return the area beneath the function fx
    :param fx: some function of x to integrate
    :param args: a tuple containing (mean, stDev, lhl, rhl)
    :return: the area beneath the function between lhl and rhl
    """
    mu, sig, lhl, rhl = args
    h = (rhl - lhl) / N
    s = fn((lhl, mu, sig)) + fn((rhl, mu, sig))
    for i in range(1, N, 2):
        s += 4 * fn((lhl + i * h, mu, sig))
    for i in range(2, N-1, 2):
        s += 2 * fn((lhl + i * h, mu, sig))
    return s * h / 3

def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """
    This funciton implements th Secant method to find the root of an equation.  You should write your equation in a form
    fcn = 0 such that when the correct value of x is selected, the fcn actually equals zero (or very close to it).
    :param fcn: the function for which we want to find the root
    :param x0: x value in neighborhood of root (or guess 1)
    :param x1: another x value in neighborhood of root (or guess x0+1)
    :param maxiter: exit if the number of iterations (new x values) equals this number
    :param xtol:  exit if the |xnewest - xprevious| < xtol
    :return: tuple with: (the final estimate of the root (most recent value of x), number of iterations)
    """
    for _ in range(maxiter):
        f0 = fcn(x0)
        f1 = fcn(x1)
        if abs(f1 - f0) < 1e-12:
            raise ValueError("Function values at x0 and x1 are too close")
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        if abs(x2 - x1) < xtol:
            return x2
        x0, x1 = x1, x2
    return x1

def GaussSeidel(Aaug, x, Niter = 15):
    """
    This should implement the Gauss-Seidel method (see page 860, Tabl 20.2) for solving a system of equations.
    :param Aaug: The augmented matrix from Ax=b -> [A|b]
    :param x:  An initial guess for the x vector. if A is nxn, x is nx1
    :param Niter:  Number of iterations to run the GS method
    :return: the solution vector x
    """
    Aaug = GE.MakeDiagDom(Aaug)
    n = len(Aaug)
    for _ in range(Niter):
        for i in range(n):
            sum1 = sum(Aaug[i][j] * x[j] for j in range(n) if j !=i)
            x[i] = (Aaug[i][-1] - sum1) / Aaug[i][i]
    return x

def main():
    '''
    This is a function I created for testing the numerical methods locally.
    :return: None
    '''
    #region testing GPDF
    fx = GPDF((0,0,1))
    print("={:0.5f}".format(fx))  # Does this match the expected value?   #added p0 for a variable
    #edregion

    #region testing Simpson
    p=Simpson(GPDF,(0,1,-5,0)) # should return 0.5
    print("p={:0.5f}".format(p))  # Does this match the expected value?
    #endregion

    #region testing Probability
    p1 = Probability(GPDF, (0,1),0,True)
    print("p1={:0.5f}".format(p1))  # Does this match the expected value?
    #endregion
    pass

#endregion

#region function calls
if __name__ == '__main__':
    main()
#endregion