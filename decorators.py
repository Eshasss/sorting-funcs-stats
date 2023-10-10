def megadec(func):
    import time
    import psutil
    def wrappere(*args, **kwargs):
        start_time = time.time()
        process = psutil.Process()
        mem_before = process.memory_info().rss
        result = func(*args, **kwargs)
        end_time = time.time()
        mem_after = process.memory_info().rss
        print(f"Функция {func.__name__} запускалась {end_time - start_time:.5f} секунд \nФункция {func.__name__} использовала {mem_after - mem_before} байтов памяти")
        return result
    return wrappere


# def memory(func):
#     import psutil
#     def wrapper(*args, **kwargs):
#         process = psutil.Process()
#         mem_before = process.memory_info().rss
#         result = func(*args, **kwargs)
#         mem_after = process.memory_info().rss
#         print(f"Функция {func.__name__} использовала {mem_after - mem_before} байтов памяти")
#         return result
#     return wrapper