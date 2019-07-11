from multiprocessing import Queue, Process
import os, time, random

def write(q):
    print('P-write %s' % os.getpid())
    for i in ['a', 'b', 'c', 'd']:
        print('Put %s in Queue' % i)
        q.put(i)
        time.sleep(random.random() * 5)

def read(q):
     print('P-read %s' % os.getpid())
     while True:
         value = q.get(True)
         print('Get %s from queue' % value)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    print('pw will be start')
    pw.start()
    print('pr will be start')
    pr.start()
    pw.join()
    pr.terminate()
    