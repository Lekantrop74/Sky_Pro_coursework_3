import Class
from utils import utils

try:
    class_list = []

    number = utils.right_input(input("Введите количество операций: "))

    sort_data = utils.sort_by_date(number)

    for i in sort_data:
        class_list.append(Class.cart_operations(i))

    for i in class_list:
        print(i.data_print_return())


except:
    print("Данные ведены некоректно")
