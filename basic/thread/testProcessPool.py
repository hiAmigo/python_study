from multiprocessing import Pool
import os, time, random

def run_proc(name):
    print('C-Process-%d-%d' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 5)
    end = time.time()
    print('C-Process-%d-%d is done, total %ds' % (name, os.getpid(), (end - start)))

if __name__ == '__main__':
    print('Parent process is %s' % os.getpid())
    p = Pool(4)
    for i in range(6):
        p.apply_async()