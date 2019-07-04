'''
函数式编程的测试文件
'''

#匿名函数
# print(list(map(lambda x: x*x, [1,2,3,4,5])))

# f = lambda x: x*x
# print(f(5))

# def build(x, y):
#     return lambda: x*y
# test_build = build(2,3)
# print(test_build())

# 装饰器
def now():
    return '2019-07-05'
f = now
print(f())
print(now.__name__)
print(f.__name__)
