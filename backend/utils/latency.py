import time


def measure_latency(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()

    latency = round(end - start, 3)
    return result, latency
