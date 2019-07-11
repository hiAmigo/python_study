import threading

local_school = threading.local()

def fun_proc():
    std = local_school.student
    print('Hello , %s in (%s)' % (std, threading.current_thread().name))

def foo(name):
    local_school.student = name
    fun_proc()

t1 = threading.Thread(target=foo, args=('Andy',), name='Thread-A')
t2 = threading.Thread(target=foo, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
