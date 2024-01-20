def square(x: int | float) -> int | float:
    """
    Returns square of x
    """
    return x**2


def pow(x: int | float) -> int | float:
    """
    Returns number to the power of itself
    """
    return x**x


def outer(x: int | float, function) -> object:
    """
    Outer function is set up to act as outer scope for closure
    -> Inner function references x from outer scope
    => x is never destroyed as long as a instance of "inner" still
    exists
    """
    def inner() -> float:
        """
        Acts as a closure
        """
        nonlocal x
        x = function(x)
        # print(inner.__closure__)
        return x
    return inner
