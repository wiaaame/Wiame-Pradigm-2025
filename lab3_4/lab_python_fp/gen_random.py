import random

def gen_random(num_count, begin, end):
    for _ in range(num_count):
        yield random.randint(begin, end)


print("\nЗадание 2")
print("Генерируем 5 случайных чисел от 1 до 3:")
for num in gen_random(5, 1, 3):
    print(num, end=' ')
print()

print("\nГенерируем 10 случайных чисел от 10 до 20:")
for num in gen_random(10, 10, 20):
    print(num, end=' ')
print()
