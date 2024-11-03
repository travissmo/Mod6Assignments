import multiprocessing
import time
import random
from datetime import datetime

def wait_and_print():
    wait_time = random.uniform(0, 1)
    time.sleep(wait_time)
    print(f"Process {multiprocessing.current_process().name} - Time: {datetime.now()}")


if __name__ == '__main__':
    processes = [multiprocessing.Process(target=wait_and_print, name=f"Process-{i+1}") for i in range(3)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

