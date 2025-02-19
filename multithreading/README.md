# Multithreading

The following topics are covered:

[01 - multithreading task](https://github.com/NicoMrs/Parallel-Computing/tree/main/multithreading/01%20-%20multithreaded%20task)
How to store data in a shared list ? Sequential option vs a multithreaded option are compared.

[02 - race condition](https://github.com/NicoMrs/Parallel-Computing/tree/main/multithreading/02%20-%20race%20condition)
How to protect a shared file with a mutex lock so that it become threads safe ?
Sequential writing, multithreaded writing with no lock and multithreaded writing with lock are compared.

[03 - ThreadPoolExecutor](https://github.com/NicoMrs/Parallel-Computing/tree/main/multithreading/03%20-%20ThreadPoolExecutor)
We will use the **ThreadPoolExecutor** class from the **concurrent.futures** module which offers a simpler API than the **threading** module.
We will compare map and submit functions.

[04 - Matrix Multiplication](https://github.com/NicoMrs/Parallel-Computing/tree/main/multithreading/04%20-%20MatriceMultiplication)
We will show a concrete example on how to multiply matrices using multithreading. Multiplying matrices is in fact a CPU bound task. We 
will show that **multithreading** doesn't enbable much gain while **multiprocessing** can offer better results.

[05 - Threaded Pipelines](https://github.com/NicoMrs/Parallel-Computing/tree/main/multithreading/05%20-%20Threaded%20Pipeline)
We will show how to generate multithreaded pipelines to download and store information about images.

