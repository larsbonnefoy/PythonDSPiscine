"""
The use of *args and**kwargs is there to make sure that any input arguments can
be accepted. The return value of a decorator is almost always the result of
calling func(*args, **kwargs), where func is the original unwrapped function.
"""


def callLimit(limit: int):
    """
    Decorator, used to impose a call limit on a function
    Executes once when we get the argument
    """

    def callLimiter(function):
        """"
        Executes once when we decorate the function
        """
        count = 0

        def limit_function(*args, **kwargs):
            """
            Runs each time we call the function
            """
            nonlocal count
            if count >= limit:
                print(
                    f"Error: <function {function.__name__} at"
                    + f"{hex(id(function))}> call to many times"
                )
            count += 1
            return function(*args, **kwargs)

        return limit_function

    return callLimiter
