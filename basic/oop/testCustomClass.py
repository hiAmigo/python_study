class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object(name:%s) ' % self.name

    def test(self):
        print('调用方法')

    def __getattr__(self, attr):
        if attr == 'score':
            return 0
        if attr == 'age':
            return lambda : 25

    def __call__(self):
        print('__call__被调用了')
s0 = Student('Lee')
s0()
# print(s0.sfsd)


class Fib:

    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a
        
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L

f = Fib()
# print(f[5])
# print(f[2:7])

class Chain:

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self.path, path))

    def __str__(self):
        return self._path

chain = Chain()
# print(chain.ststus.user.item.timeline.list)


