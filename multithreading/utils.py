# utils.py

from time import perf_counter

def perf_decorator(func):
    """ decorator to measure time taken by a func """
    
    def inner(*args, **kwargs):
        
        start = perf_counter()
        res = func(*args, **kwargs)
        end = perf_counter()
        print(f"{func.__name__} execution time {end-start:.2f}s")
        return res
        
    return inner