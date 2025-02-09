# Parallel Computing in Python

There exists mainly two ways to improve our code execution time through parallelism. One is multithreading, the other one is multiprocessing. 


### 1. multithreading
Multithreading is an interesting option when our code performs **I/O tasks**. In fact, due to the Global Interpretor Lock (GIL), which is a 
Python paradigm only one thread can be executed at time, except during I/O tasks where the GIL is released.
We can start many threads, quite cheaply and share data between them. We will explore through some examples, how we can make are code multithreaded, 
without falling in the pitfall of **race concurrency** by protecting our data with **mutex locks**.
We could also use other flavors of Python: CPython (C implementation) or Jython (Java implementation) which are not restreined by the GIL.

### 2. multiprocessing
Multiprocessing is an other way to go. With it, we can achieve full parallelism but at the cost of memory space and slower start.
This is an heavyweight option which should be considered when our code perform **CPU bound** tasks.



<p align="center">
  <img src="images/multithreading_multiprocessing.JPG?raw=true" width="580">
</p>
