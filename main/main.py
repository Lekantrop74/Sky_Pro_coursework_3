from utils import utils, Class


def __main__():
    try:
        class_list = []
        # Сколько операций будет выведенно
        number = utils.right_input(input("Введите количество операций: "))
        # Получение списка отсортированных словарей и заданным количеством
        sort_data = utils.sort_by_date(number)
        # Переобразование элементов полученного списка в экземпляры класса
        for i in sort_data:
            class_list.append(Class.cart_operations(i))
        # Вывод нужных данных по операции
        for i in class_list:
            print(i.data_print_return())


    except:
        print("Данные ведены некоректно")


if __name__ == __main__():
    __main__()
