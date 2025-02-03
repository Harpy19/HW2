#region imports
from math import sqrt, pi, exp
from NumericalMethods import GPDF, Simpson, Probability
#endregion

#region function definitions
def main():
    """
    I want to integrate the Gaussian probability density function between
    a left hand limit = (mean - 5*stDev) to a right hand limit = (c).  Here
    is my step-by-step plan:
    1. Decide mean, stDev, and c and if I want P(x>c) or P(x<c).
    2. Define args tuple and c to be passed to Probability
    3. Pass args, and a callback function (GPDF) to Probability
    4. In probability, pass along GPDF to Simpson along with the appropriate args tuple
    5. Return the required probability from Probability and print to screen.
    :return: Nothing to return, just print results to screen.
    """
    #region testing user input
    # The following code solicites user input through the CLI.
    mean1 = 100
    stDev1 = 12.5
    c1 = 105
    prob1 = Probability(GPDF, (mean1, stDev1), c1, GT=False) #copilot
    print("P(x<{:.2f}|N({},{}))={:.2f}".format(c1, mean1, stDev1, prob1)) #changed format of given code

    mean2 = 100
    stDev2 = 3
    c2 = mean2 + 2 *stDev2
    prob2 = Probability(GPDF, (mean2, stDev2), c2, GT=True) #copilot
    print("P(x>{:.2f}|N({},{}))={:.2f}".format(c2, mean2, stDev2, prob2)) #changed format of given code
    #endregion
#endregion

if __name__ == "__main__":
    main()