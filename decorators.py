from classes import MyList
import functools
def megadec(func):
    import time
    import psutil
    def wrapper(*args, **kwargs):
        start_time = time.time()
        process = psutil.Process()
        mem_before = process.memory_info().rss
        result = func(*args, **kwargs)
        end_time = time.time()
        mem_after = process.memory_info().rss
        tim = (mem_before- mem_after)
        reads = result.__read__()
        writes = result.__write__()
        print(f"Функция {func.__name__} запускалась {end_time - start_time:.5f} секунд \nФункция {func.__name__} использовала {tim} байтов памяти\n {reads} чтений, {writes} записей\n=========")
        return result
    return wrapper




# def megadec2(func):
#     import timed
#     import psutil
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         process = psutil.Process()
#         mem_before = process.memory_info().rss
#         result = func(*args, **kwargs) 
#         end_time = time.time()
#         mem_after = process.memory_info().rss
#         #reads = result[1]

#         print(f"Функция {func.__name__} запускалась {end_time - start_time:.5f} секунд \nФункция {func.__name__} использовала {mem_after - mem_before} байтов памяти\n чтений,  записей\n=========")
#         return result
#     return wrapper
# def megarec(func):
#     import time
#     import psutil
#     wr = 0
#     rd = 0
#     def wrapper(*args, **kwargs):
#         nonlocal wr, rd
#         start_time = time.time()
#         process = psutil.Process()
#         mem_before = process.memory_info().rss
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         mem_after = process.memory_info().rss
#         rd += result.__read__()
#         wr = result.__write__()
#         print(f"Функция {func.__name__} запускалась {end_time - start_time:.5f} секунд \nФункция {func.__name__} использовала {mem_after - mem_before} байтов памяти\n{rd} чтений, {wr} записей\n=========")
#         return result
#     return wrapper


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