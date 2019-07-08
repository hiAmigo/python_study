'''
函数式编程的测试文件
'''


# L=['andy', 'bob','candy']
# print(L[-2:])

#list = list(range(100))
#print(list[::2])

# s = 'ABCDEFGH'
# print(s[:3])

# L1 = []
# for n in range(1,11): 
#     L1.append(n*n)
# print(L1)
#print([x*x for x in range(1,11) if x%2 == 0])
#print([x+y for x in 'ABC' for y in '123'])

#L = ['anSf', 'SDS1', 12, None, 'EE#w']
#print([n.lower() for n in L if isinstance(n, str)])

# g = (n*n for n in range(1,11))

# for n in g:
#     print(n)

# def odd():
#     yield 1
#     print('step2')
#     yield 2
#     print('step3')

# o = odd()
# print(next(o))
# print(next(o))

# def fib(max):
#     n,a,b =0,0,1
#     while n<max:
#         yield b
#         a,b = b,a+b
#         n+=1
#     return 'down'

# g = fib(6)
# while True:
#     try:
#         x=next(g)
#         print(x)
#     except StopIteration as e:
#         print('Generator return value is' + e.value)
#         break


#杨辉三角
# def triangles():
#     p = [1]
#     while True:
#         yield p
#         p = [1]+[p[n]+p[n-1] for n in range(1,len(p))]+[1]

# n = 0
# for t in triangles():
#     print(t)
#     n = n+1
#     if n == 10:
#         break
     
# f = abs
# print(f(-10))
# print(abs(-10))

# abs = 10
# print(abs(-10))

# def f(x):
#     return x*x

# print(list(map(f, [1,2,3,4,5])))

# from functools import reduce
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# # def add(x,y):
# #     return x*10+y

# # print(reduce(add, [1,2,3,4,5]))
# def char2num(x):
#     return DIGITS[x]

# def str2int(s):
#     return reduce(lambda x,y : x*10+y, map(char2num, s))

# print(str2int('2312312312'))

# def _odd_iter_():
#     n = 1
#     while True:
#         n += 2
#         yield n

# def primes():
#     yield 2
#     it = _odd_iter_()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible(n), it)

# def _not_divisible(n):
#     return lambda x: x%n > 0

# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break

# sorted 函数
# print(sorted([-1,24,-52,2,1,-5,56], key=abs))

# print(sorted('dsSFd1sdf', key=str.lower))

#返回函数

def lazy_sum(*args):
    def sum():
        total = 0
        for n in args:
            total += n
        return total
    return sum


# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#             return i*i
#         fs.append(f)
#     return fs

# def count():
#     pr = []
#     def g(j):
#         def f():
#             return j*j
#         return f
#     for i in range(1,4):
#         pr.append(g(i))
#     return pr

# f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())

# def pr():
#     L = 1
#     def chr():
#         nonlocal L
#         L = L + 1
#         return L
#     return chr
# N = pr()
# print(N())

#匿名函数
# print(list(map(lambda x: x*x, [1,2,3,4,5])))

# f = lambda x: x*x
# print(f(5))

# def build(x, y):
#     return lambda: x*y
# test_build = build(2,3)
# print(test_build())

# 装饰器
# def now():
#     return '2019-07-05'
# f = now
# print(f())
# print(now.__name__)
# print(f.__name__)

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
    
@log
def now():
    print('2019-07-05')

print(now())
