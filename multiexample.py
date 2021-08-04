# Basic application of Multiprocessing package in Python, with simple examples
import multiprocessing
from time import sleep
import time
import os

def do_calculation(data: int):
    print('Sleeping for {} seconds at Process name {}, ID {}'.format(data/2, multiprocessing.current_process().name,  os.getpid()))
    time.sleep(data/2)
    return data * 2
def start_process():
    timestamp  = time.time() % 100
    print('Initiating at time {:.4f} s, at Process name {}, ID {}'.format(timestamp, multiprocessing.current_process().name, os.getpid()))
def do_calculation(data):
    print('Sleeping for {} seconds at Process name {}, ID {}'.format(data/2, multiprocessing.current_process().name,  os.getpid()))
    sleep(data/2)
    return data * 2


def start_process():
    timestamp  = time.time() % 100
    print('Initiating at time {:.4f} s, at Process name {}, ID {}'.format(timestamp, multiprocessing.current_process().name, os.getpid()))


if __name__ == '__main__':
    inputs = list(range(5))
    print('Input   :', inputs)

    builtin_outputs = map(do_calculation, inputs)
    print('Built-in:', builtin_outputs)
    print('Main process: Name: {}, ID: {}'.format(multiprocessing.current_process().name, os.getpid()))
    pool_size = multiprocessing.cpu_count() 

    t0 = time.time()
    pool = multiprocessing.Pool(
        processes=pool_size,
        initializer=start_process,
    )
    t0 = time.time()
    pool_outputs = pool.map(do_calculation, inputs)
    pool.close()  # no more tasks
    pool.join()  # wrap up current tasks
    t1 = time.time()

    print('Pool with map:', pool_outputs, 'time: ', t1-t0)
    print('*************')
    t0a = time.time()
    pool = multiprocessing.Pool(
        processes=pool_size,
        initializer=start_process,
    )
    pool_applyoutputs = [pool.apply(do_calculation, args = (i,)) for i in inputs]
    pool.close()  # no more tasks
    pool.join()  # wrap up current tasks
    t1a = time.time()
    print('Pool with apply:', pool_applyoutputs, 'time: ', t1a-t0a)
    print('*************')
    t0b = time.time()
    with multiprocessing.Pool(processes=pool_size, initializer=start_process) as pool:
        pool_applyprocesses = [pool.apply_async(do_calculation, args = (i,)) for i in inputs]
        pool_asyncresults = [q.get() for q in pool_applyprocesses]
    pool.join()
    t1b = time.time()
    print('Pool with apply_async:', pool_applyoutputs, 'time: ', t1b-t0b)

