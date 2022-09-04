csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""

def _read(csv):
    """Функция читает данные из файла и объединяет их в список"""
    return [x.split(';') for x in csv.split('\n')]

def _sort(data):
    """Функция сортирует данные по возрасту по возрастанию"""
    return sorted(data, key=lambda x: int(x[1]))


def _filter(data):
    """Функция фильтрует данные по возрасту, отсеивая тех, кто моложе 10 лет"""
    return [x for x in data if int(x[1]) > 10]


def get_result():
    a = (_read(csv))
    b = (_sort(a))
    return _filter(b)

if __name__ == '__main__':
    print(get_result())