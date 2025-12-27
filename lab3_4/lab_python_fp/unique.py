from gen_random import gen_random

# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.seen = set()
        self.ignore_case = kwargs.get('ignore_case', False)

    def __next__(self):
        while True:
            item = next(self.items)

            # Для сравнения используем ключ
            if self.ignore_case and isinstance(item, str):
                key = item.lower()
            else:
                key = item

            # Если элемент еще не встречался, добавляем его и возвращаем
            if key not in self.seen:
                self.seen.add(key)
                return item

    def __iter__(self):
        return self


print("\nЗадание 3")
print("Тест 1 - список с дубликатами:")
data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
for item in Unique(data):
    print(item, end=' ')
print()

print("\nТест 2 - генератор случайных чисел:")
data = gen_random(10, 1, 3)
for item in Unique(data):
    print(item, end=' ')
print()

print("\nТест 3 - строки, ignore_case=False:")
data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
for item in Unique(data):
    print(item, end=' ')
print()

print("\nТест 4 - строки, ignore_case=True:")
data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
for item in Unique(data, ignore_case=True):
    print(item, end=' ')
print()
