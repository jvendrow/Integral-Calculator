def integrate(f, a, b):
    """
    Approzimates the integral of a function from a to b using the trapezoid rule
    >>> integrate(sin, -7, 7)
    0.0
    >>> integrate(lambda x: pow(cos(x), 2) * sin(x), 0, pi())
    0.66666641
    """
    if(a > b):
        return - integrate(f, b, a)
    total = 0
    iters = 1000
    while(a <= b):
        total += (f(a) + f(a+1.0/iters)) / (2 * iters)
        a += 1.0 / iters
    return round(total, 8)

def sqrt(x):
    """
    Finds the square root of a number
    Warning: RecursionError may occur with certain numbers
    >>> sqrt(20)
    4.47213595499958
    """
    assert x >= 0, "Cannot take the square root of negative numbers"
    def f(guess):
        if(guess == x/guess):
            return guess
        else:
            return f((x/guess + guess)/2)
    return f(1)

def pi():
    """
    Returns the approximation of pi
    >>> pi()
    3.1415876535897618
    """

    total = 4.0
    d = 3.0
    toAdd = False
    while 4/d > pow(10, -5):
        if(toAdd):
            total += 4 / d
        else:
            total -= 4 / d
        toAdd = not toAdd
        d += 2
    return total

def pi_recursive(total = 4.0, d = 3.0, toAdd = False):                    
    """
    Returns an approximation of pi recursively
    Only works up to a precusion of 2 due to RecursionError
    >>> pi_recursive()
     3.136592684838816
    """ 
    if 4/d < pow(10, -2):
        return total 
    else:
        if(toAdd):
            return pi_recursive(total + 4/d, d+2, not toAdd)
        else:
            return pi_recursive(total - 4/d, d+2, not toAdd)


def e(x):
    """
    Approzimates e to the power of x
    >>> e(1)
    2.7182818011463845
    >>> e(2)
    7.3890560703259105
    >>> e(3)
    20.08553685145113
    """
    total = 1.0
    d = 1.0
    while pow(x, d)/fact(d) > pow(10, -7):
        total += pow(x, d)/fact(d)
        d += 1
    return total

def e_recursive(x, total = 1.0, d = 1.0):
    """
    Approximates e to the power of x using recursion
    >>> e_recursive(1)
    2.7180555555555554
    >>> e_recursive(2)
    7.3887125220458545
    >>> e_recursive(3)
    20.08521256087662
    """
    if pow(x, d)/fact(d) <= pow(10, -3):
        return total
    else:
        return e_recursive(x, total + pow(x, d)/fact(d), d+1)

def ln(x):
    """
    Approximates the natural log of a number
    >>> ln(5)
    1.60943799
    >>> ln(e(3))
    3.00002314
    """
    assert x > 0, "Cannot take natural log of a negative number or 0"
    return integrate(lambda n: 1/n, 1, x)

def sin(x):
    """
    Approximates the sine of x
    >>> sin(0)
    0.0
    >>> sin(pi()/2)
    0.9999999437390877
    >>> sin(5)
    -0.9589242932128198
    """
    if(x < 0):
        return -sin(-x)
    total = 0.0
    d = 1.0
    toAdd = True
    while pow(x, d)/fact(d) > pow(10, -7):
        if toAdd:
            total += pow(x, d)/fact(d)
        else:
            total -= pow(x, d)/fact(d)
        toAdd = not toAdd
        d += 2
    return total

def cos(x):
    """
    Approximates the cosine of x
    >>> cos(0)
    1.0
    >>> cos(pi())
    -1.000000003516469
    >>> cos(5)
    0.2836620929723069
    """
    x = abs(x)
    total = 1.0
    d = 2.0
    toAdd = False
    while pow(x, d)/fact(d) > pow(10, -7):
        if toAdd:
            total += pow(x, d)/fact(d)
        else:
            total -= pow(x, d)/fact(d)
        toAdd = not toAdd
        d += 2
    return total

def tan(x):
    """
    Approximates the tangent of x
    >>> tan(0)
    0.0
    >>> tan(pi()/4)
    0.9999974678354391
    """
    return sin(x) / cos(x)

def csc(x):
    """
    Approximates the cosecant of x  
    >>> csc(pi()/2)
    1.0000000562609155
    >>> csc(5)
    -1.0428351925985297
    """
    return 1 / sin(x)

def sec(x):
    """
    Approximates the secant of x
    >>> sec(0)
    1.0
    >>> sec(5)
    3.5253212352826684
    """
    return 1 / cos(x)

def cot(x):
    """
    Approximates the cotangent of x
    >>> cot(pi()/4)
    1.000002532170973
    >>> cot(3*pi()/4)
    -0.9999925682455827
    """
    return cos(x) / sin(x)
    
"""
Returns the factorial of n
>>> fact(6)
720
"""
fact = lambda n: (lambda f, n: f(f, n))(lambda f, n: n * f(f, n-1) if n > 1 else 1, n)
