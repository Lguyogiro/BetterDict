from operator import add, sub, mul, div
from collections import OrderedDict, defaultdict


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
        return merged(self, other, add)

    def __sub__(self, other):
        return merged(self, other, sub)

    def __mul__(self, other):
        return merged(self, other, mul)

    def __div__(self, other):
        return merged(self, other, div)

    def copy(self):
        return type(self)(self.items())

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


class BetterDefaultDict(BetterDict, defaultdict):
    def __init__(self, *args):
        defaultdict.__init__(self, *args)

    def copy(self):
        return defaultdict.copy(self)


class BetterOrderedDict(BetterDict, OrderedDict):
    pass


if __name__ == '__main__':
    pass
