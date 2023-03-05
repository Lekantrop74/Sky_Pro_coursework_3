import json
import datetime


def load_json():
    """ функция данных из json"""
    try:
        with open('utils/operations.json', 'r', encoding='utf-8') as operation:
            return json.load(operation)
    except:
        return 'Ошибка файла'


def transactions_executed():
    """ функция перебора json и нахождение успешных операций игнорируя пустых записей в Json"""
    data = load_json()
    data_executed = []
    # Проход по всему списку на поиск и добавление в новый список по "EXECUTED"
    for i in range(len(data)):
        try:
            if data[i]['state'] == 'EXECUTED':
                data_executed.append(data[i])
        except:
            continue
    return data_executed


def right_input(inputs):
    """Проверка на правильность ввода"""
    if inputs.isdigit():
        return int(inputs)


def sort_by_date(a):
    """ Сортировка списка выполненых операций по дате в обратном порядке
    и возврщение заданного количества элементов"""
    data_executed = transactions_executed()
    sort_name = sorted(data_executed, key=lambda x: datetime.datetime.fromisoformat(x['date']), reverse=True)
    return sort_name[:int(a)]
