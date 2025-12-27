def field(items, *args):
    assert len(args) > 0

    if len(args) == 1:
        # Если передан один аргумент - возвращаем только значения этого поля
        key = args[0]
        for item in items:
            value = item.get(key)
            if value is not None:
                yield value
    else:
        # Если передано несколько аргументов - возвращаем словари
        for item in items:
            result = {}
            for key in args:
                value = item.get(key)
                if value is not None:
                    result[key] = value
            # Если хотя бы одно поле не None, выдаем словарь
            if result:
                yield result


print("Задание 1")
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]

print("Тест 1 - один аргумент 'title':")
for value in field(goods, 'title'):
    print(value)

print("\nТест 2 - один аргумент 'price':")
for value in field(goods, 'price'):
    print(value)

print("\nТест 3 - два аргумента 'title', 'price':")
for value in field(goods, 'title', 'price'):
    print(value)
