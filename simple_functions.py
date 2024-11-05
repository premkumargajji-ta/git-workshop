# Custom python functions

def double_number(a):
    """
    Doubles the number

    Parameter: int or float
    Returns: int or float (double of the given number)

    Example: 
    >>> double_number(2)
    4
    >>> double_number(2.5)
    5.0
    """
    print(f'value before double_number(): {a}')
    result = a+a
    print(f'value after double_number(): {result}')
    return result

def square_number(a):
    """
    Squares a given number
    
    Parameter: int or float
    Returns: int or float

    Example: 
    >>> square_number(2)
    4
    """
    print(f'value before square_number(): {a}')
    result = a*a
    print(f'value after square_number(): {result}')
    return result

