from utils.main import GetData, Format_Obj

from datetime import datetime

from collections import Counter


class SimpleReport(GetData):
    def __init__(self, list_of_dicts=None):
        self.list_of_dicts = list_of_dicts or list()
        self.path = "data/inventory_20200823.json"

    def f_generate(self):
        data = GetData(self.path)
        datas = data.f_by_get_data_json()
        data_f = ""
        data_v = ""
        data_de_fabricacao = datetime.strptime(data_f, "%y/%m/%d")
        validade = datetime.strptime(data_v, "%y/%m/%d")
        name = Counter(empresa["nome_da_empresa"] for empresa in datas)

        greater_amount_of_stocks = name[max(name, key=name.get)]

        for obj in datas:
            for keys, values in obj:
                if keys in "data_de_fabricacao" and values < data_de_fabricacao:
                    data_f = values
                if keys in "data_de_validade" and values > validade:
                    data_v = values
        obj_output = Format_Obj(data_de_fabricacao, validade, greater_amount_of_stocks)
        return obj_output.f_hand_over_keys()


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
