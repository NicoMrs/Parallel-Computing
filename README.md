# Parallel Computing in Python

Concurrency enables a computer to do many different things seemingly at the same time by rapidly switching which program is running. 
That's how threads work. Only one is executed at a time, while the other are sleeping in a waiting queue. 
True parallelism is achieved through multiprocessing where multiple cores are used for the tasks.

### 1. multithreading
Multithreading is an interesting option when our code performs **I/O tasks**. Due to the Global Interpretor Lock (GIL), which is a 
Python paradigm, only one thread can be executed at time. However during I/O tasks the GIL is released. So we can leverage that behaviour
to make programs run faster through multithreading when tasks are mostly I/O.
We can start many threads, quite cheaply and share data between them. Through some examples, we will show how to make our code multithreaded, 
without falling in the pitfall of **race concurrency** by protecting our data with **mutex locks**.
We could also use other flavors of Python: CPython (C implementation) or Jython (Java implementation) which are not restreined by the GIL.

### 2. multiprocessing
Multiprocessing is an other way to go. With it, we can achieve full parallelism but at the cost of memory space and slower start.
This is an heavyweight option which should be considered when our code perform **CPU bound** tasks.


<p align="center">
  <img src="images/multithreading_multiprocessing.JPG?raw=true" width="580">
</p>
