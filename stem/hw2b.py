#region imports
from NumericalMethods import Secant
from math import cos #math imports used
#endregion

#region function definitions
def fn1(x):
    return x - 3 * cos(x) #equation listed below

def fn2(x):
    return cos(2 * x) * x**3  #equation listed below

def main():
    """
       fn1:  x-3cos(x)=0; with x0=1, x1= 2, maxiter = 5 and xtol = 1e-4
       fn2:  cos(2x)*x**3; with x0=1, x1= 2, maxiter = 15 and xtol = 1e-8
       fn2:   with x0=1, x1= 2, maxiter = 3 and xtol = 1e-8

       I observe that for functions 2 and 3, the answer should be pi/2 or about 1.57
    :return: nothing, just print results
    """
    r1 = Secant(fn1, 1, 2, 5,1e-4) #given
    r2 = Secant(fn2, 1,2,15, 1e-8) #given
    r3 = Secant(fn2,1,2,3,1e-8)    #given
    print("root of fn1 = {:.4f}, after {} iterations".format(r1, 5)) #changed print to this format
    print("root of fn2 (maxiter=15, xtol=1e-8) = {:.8f}, after {} interations".format(r2, 15)) #copilot
    print("root of fn2 (maxiter=3, xtol=1e-8) = {:.8f}, after {} interations".format(r3, 3))   #copilot
    #etc.
    pass
#endregion

if __name__=="__main__":
    main()