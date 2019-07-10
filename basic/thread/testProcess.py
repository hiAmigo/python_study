from multiprocessing import Process
import time, random, os

def run_child(name):
    print('Child process is (name:%s, %s)' % (name, os.getpid()))
    start = time.time()
    

if __name__ == '__main__':
    print('Parent process is %s' % os.getpid())
    p = Process(target=run_child, args=('test',))
    print('Child process will be start')
    p.start()
    p.join()
    print('Parent process is done')