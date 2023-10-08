def count(f):
    called = 0

    def wrapped(*args, **kwargs):
        nonlocal called
        called += 1
        return f(*args, **kwargs), called
    print(called)
    return wrapped

def benchmark(iters=1):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for _ in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print("[*] Среднее время выполнения: {} секунд.".format(total / iters))
            return return_value

        return wrapper

    return actual_decorator