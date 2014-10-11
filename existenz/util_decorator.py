"""Utility decorators."""
from decorator import decorator


def memoize(f):
    f.cache = {}
    return decorator(_memoize, f)


def _memoize(func, *args, **kwargs):
    """A args based function cache."""
    if kwargs:
        key = args, frozenset(kwargs.iteritems())
    else:
        key = args
    cache = func.cache
    if key in cache:
        return cache[key]
    else:
        cache[key] = result = func(*args, **kwargs)
        return result
