class Fib(object):
    def __init__(self, num):
        a, b, L = 0, 1, []
        for i in range(num):
            L.append(a)
            a, b = b, a+b
        self.numbers = L

    def __repr__(self):
        return repr(self.numbers)

    def __len__(self):
        return len(self.numbers)

f = Fib(100)
print f
print len(f)