def intSqrt(n: int):
    """
    Returns the integer square root of an integer number, 
    If the number is not a perfect square, the rounded down value of the true sqare root is returned
    The computation is performed entirely with integer values allowing arbitrary large values to be square rooted

    Parameters:
        n (int): the number to be square rooted
    
    Returns:
        (int): the integer square root of n
    
    Raises:
        TypeError: if n is not of type int
        ValueError: if n is negative
    """
    
    if n < 0:
        raise ValueError
    
    if type(n) != int:
        raise TypeError

    x = n
    y = (x + 1) // 2
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def isPerfectSqare(number: int):
    """
    Returns whether a number is a perfect square

    Parameters:
        number (int): number to be tested

    Returns:
        (bool): whether a number is a perfect square
    
    Raises:
        TypeError: if number is not of type int
        ValueError: if number is negative
    """

    return intSqrt(number) ** 2 == number


def isFibonacci(number: int):
    """
    Returns whether a number is contained in the Fibonacci sequence
    A positive integer is included in the Fibonacci sequence if:
    (5 * number ^ 2 - 4) is a perfect square and/or (5 * number ^ 2 + 4) is a perfect square
    The computation is performed entirely with integer values allowing arbitrary large values to be tested

    Parameters:
        number (int): number to be tested

    Returns:
        (bool): whether a number is a perfect square
    
    Raises:
        TypeError: if number is not of type int
        ValueError: if number is negative
    """

    if type(number) != int:
        raise TypeError
    elif number < 0:
        raise ValueError

    products = 5 * number ** 2
    return products > 4 and isPerfectSqare(products - 4) or isPerfectSqare(products + 4)
