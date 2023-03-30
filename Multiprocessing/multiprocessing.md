
1. simple example 

```python
import multiprocessing
import time


def square(n, result, index):
    """Calculate the square of a number."""
    print(f"Calculating the square of {n}")
    time.sleep(1)
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
    numbers = range(0, 5000) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    squared_numbers = parallel_square(numbers)
    print(f"Squared numbers: {squared_numbers}")

```