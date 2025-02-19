from time import perf_counter
from concurrent.futures import ProcessPoolExecutor


def timeit(func):
    """ decorator that times a function """

    def inner(*args, **kwargs):
        start = perf_counter()
        res = func(*args, **kwargs)
        end = perf_counter()
        print(f"time taken {end - start:.2f}s")
        return res

    return inner


def row_work(args):
    """ return product of row time a matrice """
    res = []
    row, mat_B = args
    for j in range(len(mat_B)):
        a = 0
        for i in range(len(row)):
            a += row[i] * mat_B[i][j]
        res.append(a)
    return res


def full_matrix_product(args):
    mat_A, mat_B, i = args
    mat = []
    for row in mat_A:
        res = row_work((row, mat_B))
        mat.append(res)
    print(f"process {i} is done")
    return i


@timeit
def execute_in_multiprocess(mat_A, mat_B):
    pool = ProcessPoolExecutor()
    args = ((mat_A, mat_B, i) for i in range(10))
    result = list(pool.map(full_matrix_product, args))
    return result