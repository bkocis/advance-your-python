import multiprocessing


def square(n):
    """Calculate the square of a number."""
    return n * n


def square_chunk(chunk, queue):
    squared_chunk = [square(n) for n in chunk]
    queue.put(squared_chunk)


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
    numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    num_cores = 4
    squared_numbers = parallel_square(numbers, num_cores)
    print(f"Squared numbers: {squared_numbers}")