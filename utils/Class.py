import datetime


class cart_operations:
    """ Принимает данные по операции и делает из него экземляр класса
    __init__(self, list_operation) принимает словарь
    data_prints(self) преобразует данные в новый словарь с нужными ключами и возвращает его в self.data_operations
    date_write(self) берёт дату перевода и записывает её в новый словарь
    data_description(self) записывает тип перевода
    data_from(self) Записывает от кого произошёл перевод
    data_to(self) записывает куда произошёл перевод
    data_hide_from(self) скрывает номер карты от кого произошёл перевод
    data_hide_to(self) скрывает счёт куда произошёл перевод
    money(self) записывает валюту перевода
    data_print_return(self) возвращает строкой все неоходимые данные записанные в self.data_operations
"""

    def __init__(self, list_operation):
        self.data_operations = {}
        self.list_operation = list_operation


    def data_prints(self):
        self.date_write()
        self.data_description()
        self.data_from()
        self.data_to()
        self.data_hide_from()
        self.data_hide_to()
        self.money()

        return self.data_operations

    def date_write(self):
        date = datetime.datetime.fromisoformat(self.list_operation["date"]).date()
        self.data_operations["date"] = f"{date.day}.{date.month}.{date.year}"

    def data_description(self):
        self.data_operations["description"] = self.list_operation["description"]

    def data_from(self):
        from_name = ""
        from_number = ""
        try:
            for i in self.list_operation["from"]:
                if i.isdigit():
                    from_number += i
                else:
                    from_name += i
            self.data_operations["from_name"] = from_name
            self.data_operations["from_number"] = from_number
        except:
            pass

    def data_to(self):
        to_name = ""
        to_number = ""
        try:
            for i in self.list_operation["to"]:
                if i.isdigit():
                    to_number += i
                else:
                    to_name += i
            self.data_operations["to_name"] = to_name
            self.data_operations["to_number"] = to_number
        except:
            pass

    def data_hide_from(self):
        try:
            split_word = ""
            split_number = 0
            self.data_operations["from_number"] = self.data_operations["from_number"][0:6] + ((len(
                self.data_operations["from_number"]) - 10) * "*") + self.data_operations["from_number"][-5:-1]
            for i in self.data_operations["from_number"]:
                split_word += i
                split_number += 1
                if split_number % 4 == 0:
                    split_word += " "
            self.data_operations["from_number"] = split_word
        except:
            pass

    def data_hide_to(self):
        self.data_operations["to_number"] = 2 * "*" + self.data_operations["to_number"][-5:-1]

    def money(self):
        self.data_operations['amount'] = self.list_operation["operationAmount"]["amount"]
        self.data_operations['currency'] = self.list_operation["operationAmount"]["currency"]["name"]

    def data_print_return(self):
        self.data_prints()
        if "from_name" in self.data_operations:
            return f"{self.data_operations['date']} {self.data_operations['description']}\n" \
                   f"{self.data_operations['from_name']} {self.data_operations['from_number']} -> " \
                   f"{self.data_operations['to_name']} {self.data_operations['to_number']}\n" \
                   f"{self.data_operations['amount']} {self.data_operations['currency']}\n"
        else:
            return f"{self.data_operations['date']} {self.data_operations['description']}\n" \
                   f"{self.data_operations['to_name']} {self.data_operations['to_number']}\n" \
                   f"{self.data_operations['amount']} {self.data_operations['currency']}\n"
