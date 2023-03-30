
### Which is better to apply in python: multiprocessing or multi-threading?

The choice between using multiprocessing or multithreading in Python depends on the specific task at hand and the characteristics of your hardware.

In general, multiprocessing is better suited for CPU-bound tasks, where the primary bottleneck is the CPU's processing power. It can take advantage of multiple cores in your machine, allowing for parallel processing of different parts of the task, which can significantly speed up the execution time.

On the other hand, multithreading is better suited for I/O-bound tasks, where the primary bottleneck is waiting for input/output operations to complete, such as reading or writing files, accessing a network, or interacting with a database. In these cases, using threads can allow for better use of the CPU while waiting for I/O operations to complete.

It's also important to note that due to the global interpreter lock (GIL) in Python, multithreading may not provide as much of a performance boost as multiprocessing, especially for CPU-bound tasks. The GIL restricts the execution of multiple threads simultaneously, so only one thread can execute Python bytecode at a time. However, this limitation does not apply to multiprocessing, as each process has its own interpreter and memory space.

Overall, the best approach depends on the specific problem you're trying to solve and the characteristics of your hardware. As a rule of thumb, if your task involves heavy CPU usage, go for multiprocessing. If it involves mostly I/O operations, multithreading may be more suitable.


1. Simple example 

```python
import multiprocessing


def square(n, result, index):
    """Calculate the square of a number."""
    print(f"Calculating the square of {n}")
    result[index] = n * n


def parallel_square(numbers):
    """Parallelize the square calculation using multiprocessing."""
    process_count = len(numbers)
    result = multiprocessing.Array('i', process_count)
    processes = []

    for i, n in enumerate(numbers):
        p = multiprocessing.Process(target=square, args=(n, result, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    return list(result)


if __name__ == "__main__":
    numbers = range(0, 5000)
    squared_numbers = parallel_square(numbers)
    print(f"Squared numbers: {squared_numbers}")

```

Using the parameter to set specific number of cores used:

```python
@timeit
def parallel_square(numbers, num_cores):
    """Parallelize the square calculation using multiprocessing."""
    process_count = min(num_cores, len(numbers))
    result = multiprocessing.Array('i', len(numbers))

    chunk_size = len(numbers) // process_count
    extra = len(numbers) % process_count
    processes = []

    start = 0
    for i in range(process_count):
        end = start + chunk_size + (1 if extra > 0 else 0)
        extra -= 1

        p = multiprocessing.Process(
            target=square_chunk,
            args=(numbers[start:end], result, start)
        )
        processes.append(p)
        p.start()
        start = end

    for p in processes:
        p.join()

    return list(result)


def square_chunk(chunk, result, offset):
    for i, n in enumerate(chunk):
        print(f"Calculating the square of {n}")
        time.sleep(1)
        result[i + offset] = n * n


if __name__ == "__main__":
    numbers = range(0, 50)
    num_cores = 5
    squared_numbers = parallel_square(numbers, num_cores)
    print(f"Squared numbers: {squared_numbers}")
```

Using queue to store the output of a function that has been run in parallel

```python

def square(n):
    """Calculate the square of a number."""
    print(f"Calculating the square of {n}")
    time.sleep(1)
    return n * n


def square_chunk(chunk, queue):
    squared_chunk = [square(n) for n in chunk]
    queue.put(squared_chunk)


@timeit
def parallel_square(numbers, num_cores):
    """Parallelize the square calculation using multiprocessing."""
    process_count = min(num_cores, len(numbers))
    result_queue = multiprocessing.Queue()

    chunk_size = len(numbers) // process_count
    extra = len(numbers) % process_count
    processes = []

    start = 0
    for i in range(process_count):
        end = start + chunk_size + (1 if extra > 0 else 0)
        extra -= 1

        p = multiprocessing.Process(
            target=square_chunk,
            args=(numbers[start:end], result_queue)
        )
        processes.append(p)
        p.start()
        start = end

    for p in processes:
        p.join()

    squared_numbers = []
    while not result_queue.empty():
        squared_numbers.extend(result_queue.get())

    return squared_numbers


if __name__ == "__main__":
    numbers = range(0, 50)
    num_cores = 10
    squared_numbers = parallel_square(numbers, num_cores)
    print(f"Squared numbers: {squared_numbers}")

```

A timing utility can be defined as:

```python
import time

def timeit(method):
    def timed(*args, **kw):
        start = time.time()
        result = method(*args, **kw)
        end = time.time()
        timing = end - start
        print(f'<<<TIMING>>> {method.__name__}  {timing} sec')
        return result
    return timed
```