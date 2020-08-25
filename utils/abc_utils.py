from abc import ABC, abstractmethod

import json

import csv


class I_Read_Json_CSV_XML(ABC):
    @abstractmethod
    def f_by_get_data_json():
        """ pegar dados do arquivo json """

    @abstractmethod
    def f_by_get_data_csv():
        """ pegar dados do arquivo json """


class I_Factory_Report(ABC):
    @abstractmethod
    def f_deliver_formatted_report():
        """ entrega as keys do objeto de output """


class I_Factory_Report_Complete(ABC):
    @abstractmethod
    def f_deliver_formatted_report():
        """ entrega as keys do objeto de output """


class GetData(I_Read_Json_CSV_XML):
    def __init__(self, path):
        self.path = path

    def f_by_get_data_json(self):
        data = []
        with open(self.path) as file:
            obj = json.load(file)
            for arq in obj:
                data.append(arq)
        return data

    def f_by_get_data_csv(self):
        data = []
        with open(self.path, "r") as file_csv:
            rd = csv.DictReader(file_csv, delimiter=",")
            for arq in rd:
                data.append(arq)
        return data


class Format_Report_Simple(I_Factory_Report):
    def __init__(self, fabricacao, validade, nome_da_empresa):
        self.fabricacao = fabricacao
        self.validade = validade
        self.nome_da_empresa = nome_da_empresa

    def f_deliver_formatted_report(self):
        val = f"""
            Data de fabricação mais antiga → {self.fabricacao}
            Data de validade mais próxima → {self.validade}
            Empresa com maior quantidade
            de produtos estocados → {self.nome_da_empresa}
            """
        return val


class Format_Report_Complete(I_Factory_Report_Complete):
    @staticmethod
    def f_deliver_formatted_report(report_simple, counter):
        str_report_return = f"""\033[1;32m
        {report_simple}
        \n
        Produtos estocados por empresa:
        \033[1;35m
        """
        for inc, amount in counter.items():
            reports = f" - {inc}: {amount}"
            str_report_return += f"\033[1;35m{reports}\n"
        return str_report_return


""" verificar se o getdata é um quer dizer herança.
especilizar um comportamento """
""" tem um, somente composição """
