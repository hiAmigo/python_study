'''
函数式编程的测试文件
'''
from functools import wraps
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

# def new_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kw):
#         if not can_run:
#             return 'Function will not run'
#         return func(*args, **kw)
#     return wrapper

# @new_decorator
# def a_func():
#     return('Function is running')

# can_run = True
# print(a_func())

# can_run = False
# print(a_func())

# a_func()
# a_func = new_decorator(a_func)
# print(a_func.__name__)

def logit(logfile='C:/Users/Administrator/Desktop/Study/python_study/basic/functional_programming/out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            log_string = func.__name__ + ' was called'
            print(log_string)
            #打开logfile并写入指定内容
            with open(logfile, 'a') as opened_file:
                #将日志写入文件
                opened_file.write(log_string + '\n')
            return func(*args, **kw)
        return wrapper
    return logging_decorator

@logit()
def myfunc1():
    pass

myfunc1()

@logit(logfile='C:/Users/Administrator/Desktop/Study/python_study/basic/functional_programming/func2.log')
def myfunc2():
    pass
 
myfunc2()



