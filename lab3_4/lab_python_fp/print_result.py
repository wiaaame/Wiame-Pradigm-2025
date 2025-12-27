def print_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(func.__name__)

        if isinstance(result, list):
            # Если результат - список, выводим элементы в столбик
            for item in result:
                print(item)
        elif isinstance(result, dict):
            # Если результат - словарь, выводим ключи и значения через =
            for key, value in result.items():
                print(f'{key} = {value}')
        else:
            # Иначе просто выводим результат
            print(result)

        return result

    return wrapper


@print_result
def test_1():
    return 1

@print_result
def test_2():
    return 'iu5'

@print_result
def test_3():
    return {'a': 1, 'b': 2}

@print_result
def test_4():
    return [1, 2]

print("\nЗадание 5")
print('!!!!!!!!')
test_1()
test_2()
test_3()
test_4()
