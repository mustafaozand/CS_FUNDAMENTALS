class Value:

    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self._prev = set(_children)
        self._op = _op

    def __repr__(self):
        return f"Value(data = {self.data})"
    
    def __add__(self, other):
        out = Value(self.data + other.data, (self, other), '+')
        return out
    
    def __mul__(self, other):
        out = Value(self.data * other.data, (self, other), '*')
        return out


def main():
    a = Value(2.0)
    b = Value(-3.0)
    c = Value(10.0)
    d = a * b + c

    return d._prev

if __name__ == "__main__":
    print(main())