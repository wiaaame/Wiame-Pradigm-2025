import time
from contextlib import contextmanager

# Способ 1: На основе класса
class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time.time() - self.start_time
        print(f'time: {elapsed_time:.2f}')


# Способ 2: С использованием библиотеки contextlib
@contextmanager
def cm_timer_2():
    start_time = time.time()
    try:
        yield
    finally:
        elapsed_time = time.time() - start_time
        print(f'time: {elapsed_time:.2f}')


print("\nЗадание 6")
print("Тест cm_timer_1:")
with cm_timer_1():
    time.sleep(2.5)

print("\nТест cm_timer_2:")
with cm_timer_2():
    time.sleep(1.5)
