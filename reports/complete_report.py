from collections import Counter
from .simple_report import SimpleReport
import re


class CompleteReport:
    def __init__(self, list_os_dicts):
        self.list_os_dicts = list_os_dicts
        self.module_date = "%Y-%m-%d"

    def generate(self):
        SimpleReport(self.list_os_dicts).generate()
        companies_and_products = Counter(
          empresa["nome_da_empresa"]
          for empresa in self.list_os_dicts
        )
        array_of_companies_and_products = str(
            companies_and_products
            ).split("'")
        counter = 0
        del array_of_companies_and_products[0]
        print("Produtos estocados por empresa:")
        for element in array_of_companies_and_products:
            if counter % 2 != 0:
                nmb = re.findall(r'\d+', element)
                if nmb:
                    print(f"- {array_of_companies_and_products[counter - 1]}: {nmb[0]}")
            counter += 1
