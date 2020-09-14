from datetime import datetime
from collections import Counter


class SimpleReport:
    def __init__(self, list_os_dicts):
        self.list_os_dicts = list_os_dicts
        self.module_date = "%Y-%m-%d"

    def generate(self):
        name = Counter(
          empresa["nome_da_empresa"]
          for empresa in self.list_os_dicts
        )
        oldest_fabricate = self.filter_fabricate_date()
        near_validate = self.filter_validate_date()
        msg = self.generate_return_message(
          name,
          oldest_fabricate,
          near_validate
        )
        return print(msg)

    def filter_validate_date(self):
        biggest_date = '0000-00-00'
        for dict_value in self.list_os_dicts:
            if str(dict_value["data_de_validade"]) > biggest_date:
                biggest_date = dict_value["data_de_validade"]
        return biggest_date

    def filter_fabricate_date(self):
        less_date = datetime.today().date()
        for dict_value in self.list_os_dicts:
            if str(dict_value["data_de_fabricacao"]) < less_date:
                less_date = dict_value["data_de_fabricacao"]
        return less_date

    def generate_return_message(name, oldest_fabricate, near_validate):
        fabricate_msg = f"Data de fabricação mais antiga: {oldest_fabricate}"
        validate_msg = f"Data de validade mais próxima: {near_validate}"
        name_mg = f"Empresa com maior quantidade de produtos estocados: {name}"
        return (fabricate_msg, '\n', validate_msg, '\n', name_mg)
