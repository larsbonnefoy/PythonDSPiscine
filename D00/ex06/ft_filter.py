def ft_filter(func, iterable):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the items that are true
    """
    if func is None:
        res = [x for x in iterable if x]
    else:
        res = [x for x in iterable if func(x)]
    return iter(res)
