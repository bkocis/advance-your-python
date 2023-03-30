import multiprocessing
import time


def timeit(method):
    def timed(*args, **kw):
        start = time.time()
        result = method(*args, **kw)
        end = time.time()
        timing = end - start
        print(f'<<<TIMING>>> {method.__name__}  {timing} sec')
        return result # , timing
    return timed


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
