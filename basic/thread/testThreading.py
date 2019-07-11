import threading, time, os, multiprocessing

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(2)
    print('thread %s is stoped!' % threading.current_thread().name)

print('begin %s ' % os.getpid())
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('end %s ' % os.getpid())

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance += n
    balance -= n

def run_thread(n):
    try:
        lock.acquire()
        for i in range(1000000):
            change_it(n)
    finally:
        lock.release()


t1 = threading.Thread(target=run_thread, args=(8,))
t2 = threading.Thread(target=run_thread, args=(3,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

# def loop():
#     x = 0
#     while True:
#         x = x ^ 1

# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()