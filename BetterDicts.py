import sys
import numbers
from collections import OrderedDict, defaultdict, Counter
from operator import add, sub, mul

if sys.version_info[0] == 3:
    from operator import truediv
else:
    from operator import div as truediv


def merged(d1, d2, func=None):
    """
    update a copy of d1 with d2. For evey key they have in
    common, combine the respective values using func.
    """
    d = d1.copy()
    if func is None:
        d.update(d2)
    else:
        for k in d2:
            if k in d:
                d[k] = func(d[k], d2[k])
            else:
                d[k] = d2[k]

    return d


class BetterDict(dict):
    def __add__(self, other):
        if isinstance(other, int):
            return self.__byscalar(other, add)
        return merged(self, other, add)

    def __div__(self, other):
        if isinstance(other, numbers.Real):
            return self.__byscalar(other, div)
        return merged(self, other, div)

    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            return self.__byscalar(other, mul)
        return merged(self, other, mul)

    def __radd__(self, other):
        return self.__add__(other)

    def __rdiv__(self, other):
        if isinstance(other, numbers.Real):
            return self.__byscalar(other, div, right=True)
        else:
            return merged(other, self, div)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __rsub__(self, other):
        if isinstance(other, numbers.Real):
            return self.__byscalar(other, sub, right=True)
        else:
            return merged(other, self, sub)

    def __sub__(self, other):
        if isinstance(other, numbers.Real):
            return self.__byscalar(other, sub)
        return merged(self, other, sub)

    def __byscalar(self, scalar, op, right=False):
        type_ = type(self)
        if right:
            return type_({k: op(scalar, v) for k, v in self.items()})
        else:
            return type_({k: op(v, scalar) for k, v in self.items()})

    def copy(self):
        return type(self)(self.items())

    def difference(self, other):
        return type(self)({k: self[k] for k in self if k not in other})

    def intersection(self, other, func=lambda a, b: [a, b]):
        d = {k: func(self[k], other[k]) for k in self if k in other}
        return type(self)(d)

    def keys(self):
        return set(super(BetterDict, self).keys())

    def merge(self, other, func=None):
        """
        In-place update of self with other. When they have a key in common,
        combine their values using func.
        """
        if func is None:
            self.update(other)
        else:
            for k in other:
                if k in self:
                    self[k] = func(self[k], other[k])
                else:
                    self[k] = other[k]

    def union(self, other, func=lambda a, b: [a, b]):
        return merged(self, other, func=func)


class BetterDefaultDict(BetterDict, defaultdict):
    def __init__(self, arg):
        if issubclass(type(arg), dict):
            default_factory = type(arg.itervalues().next())
            defaultdict.__init__(self, default_factory)
            for k, v in arg.iteritems():
                self[k] = v
        else:
            defaultdict.__init__(self, arg)

    def copy(self):
        return defaultdict.copy(self)


class BetterOrderedDict(BetterDict, OrderedDict):
    pass


class BetterCounter(BetterDict, Counter):
    def __init__(self, *args):
        Counter.__init__(self, *args)

    @classmethod
    def fromkeys(cls, *args):
        BetterCounter(dict.fromkeys(*args))


if __name__ == '__main__':
    pass
