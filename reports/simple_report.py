from datetime import datetime
from collections import Counter
from utils.messages import generate_return_message


class SimpleReport:
    def __init__(self, list_os_dicts=None):
        self.list_os_dicts = list_os_dicts or []
        self.module_date = "%Y-%m-%d"

    def generate(self):
        name = Counter(
          empresa["nome_da_empresa"]
          for empresa in self.list_os_dicts
        )
        oldest_fabricate = self.filter_fabricate_date()
        near_validate = self.filter_validate_date()
        msg = generate_return_message(
          name,
          oldest_fabricate,
          near_validate
        )
        return print(*msg, sep='\n')

    def filter_validate_date(self):
        biggest_date = '0000-00-00'
        for dict_value in self.list_os_dicts:
            if str(dict_value["data_de_validade"]) > biggest_date:
                biggest_date = dict_value["data_de_validade"]
        return biggest_date

    def filter_fabricate_date(self):
        less_date = datetime.today().date()
        for dict_value in self.list_os_dicts:
            if str(dict_value["data_de_fabricacao"]) < str(less_date):
                less_date = dict_value["data_de_fabricacao"]
        return less_date
