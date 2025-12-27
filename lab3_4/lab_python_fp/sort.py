data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

print("\nЗадание 4")
def sort():
    # Способ 1: С использованием lambda-функции
    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print("С lambda:", result_with_lambda)
sort()
# Способ 2: Без использования lambda-функции
result = sorted(data, key=abs, reverse=True)
print("Без lambda:", result)
