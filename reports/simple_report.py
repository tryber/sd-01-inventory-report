from utils.abc_utils import Format_Report_Simple

from datetime import datetime

from collections import Counter


class SimpleReport:
    def __init__(self, list_of_dicts=None):
        self.list_of_dicts = list_of_dicts or []
        self.module_date = "%Y-%m-%d"

    def _f_date(self, value):
        return datetime.strptime(value, self.module_date).date()

    def f_generate(self, data):
        oldest_data_fabricacao = self._f_date(data[0]["data_de_fabricacao"])

        newest_data_validade = self._f_date(data[0]["data_de_validade"])

        name = Counter(empresa["nome_da_empresa"] for empresa in data)

        greater_of_stocks = name[max(name, key=name.get)]

        for obj in list(data):
            cur_data_fabricacao = self._f_date(obj.get("data_de_fabricacao"))
            curr_data_validade = self._f_date(obj.get("data_de_validade"))

            if cur_data_fabricacao < oldest_data_fabricacao:
                oldest_data_fabricacao = cur_data_fabricacao
            if curr_data_validade > newest_data_validade:
                newest_data_validade = curr_data_validade

        report_output = Format_Report_Simple(
            oldest_data_fabricacao, newest_data_validade, greater_of_stocks
        )
        return report_output.f_deliver_formatted_report()


datass = {
    "id": 1,
    "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
    "nome_da_empresa": "Forces of Nature",
    "data_de_fabricacao": "2020-07-04",
    "data_de_validade": "2023-02-09",
    "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
    "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices phasellus",
}


"""
_ e __ são convenções do Python,
sendo que o _ é o equivalente ao protected e o __ é equivalente ao private.
Tudo que está com _ é porque precisa ser utilizado na subclasse e
tudo que está com __ é porque só precisa ser utilizado na superclasse.

"""
