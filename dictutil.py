class BetterDict(dict):
    def __add__(self, other):
        pass
    
    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __div__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __lt__(self, other):
        pass

    def merge(self, other, func=None):
        if func is None:
            self.update(other)
        for k in other:
            if k in self:
                self[k] = func(self[k], other[k])
            else:
                self[k] = other[k]

