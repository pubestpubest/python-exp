# Concurrency in Python

import threading
import multiprocessing
import asyncio

# Using threads
def print_numbers():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()

# Using multiprocessing
def print_numbers_process():
    for i in range(5):
        print(i)

process = multiprocessing.Process(target=print_numbers_process)
process.start()
process.join()

# Using asynchronous programming
async def print_numbers_async():
    for i in range(5):
        print(i)

asyncio.run(print_numbers_async())
