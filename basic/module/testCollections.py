from collections import namedtuple, deque, defaultdict, OrderedDict, Counter
# Point = namedtuple('Point1', ['x', 'y'])
# p = Point(1,2)
# print(p.x)

# print(isinstance(p, Point))
# print(isinstance(p, tuple))

# d = deque(['a', 'b', 'c'])
# d.append('x')
# d.popleft()
# print(d)

# dd = defaultdict(lambda: 'N/A')
# dd['key1'] = 'abc'
# print(dd['key2'])

# od = OrderedDict([('d', 1), ('b', 2), ('c', 3), ('a', 4)])
# print(od)
# print(list(od.keys()))


c = Counter()
c.update('asdfienwdsaqwrwadfasafksafnkaskq qasfasfa asfsadfsaq[k')
# for ch in 'asdfienwdsaqwrwadfasafksafnkaskq qasfasfa asfsadfsaq[k':
#     c[ch] += 1

print(c)