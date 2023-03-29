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


# def square(n, result, index):
#     """Calculate the square of a number."""
#     print(f"Calculating the square of {n}")
#     time.sleep(1)
#     result[index] = n * n

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
    numbers = range(0, 50) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    num_cores = 5
    squared_numbers = parallel_square(numbers, num_cores)
    # print(f"Squared numbers: {squared_numbers}")
    print("end")
