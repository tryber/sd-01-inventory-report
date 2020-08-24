from abc import ABC, abstractmethod

import json


class I_Read_Json(ABC):
    @abstractmethod
    def f_by_get_data_json():
        """ pegar dados do arquivo json """


class I_Factory(ABC):
    @abstractmethod
    def f_hand_over_keys():
        """ entrega as keys do objeto de output """


class GetData(I_Read_Json):
    def __init__(self, path):
        self.path = path

    def f_by_get_data_json(self):
        data = []
        with open(self.path) as file:
            obj = json.load(file)
            for arq in obj:
                data.append(arq)
        return data


class Format_Obj(I_Factory):
    def __init__(self, fabricacao, validade, nome_da_empresa):
        self.fabricacao = fabricacao
        self.validade = validade
        self.nome_da_empresa = nome_da_empresa

    def f_hand_over_keys(self):
        val = f"""
            Data de fabricação mais antiga → {self.fabricacao}
            Data de validade mais próxima → {self.validade}
            Empresa com maior quantidade
            de produtos estocados → {self.nome_da_empresa}
        """
        return val


""" verificar se o getdata é um quer dizer herança. 
especilizar um comportamento """
""" tem um, somente composição """
# class Keys_By_create(I_Factory):
#     def __init__(
#         self,
#         id,
#         nome_do_produto,
#         nome_da_empresa,
#         data_de_fabricacao,
#         data_de_validade,
#         numero_de_serie,
#         instrucoes_de_armazenamento,
#     ):
#         self.id = id
#         self.nome_do_produto = nome_do_produto
#         self.nome_da_empresa = nome_da_empresa
#         self.data_de_fabricacao = data_de_fabricacao
#         self.data_de_validade = data_de_validade
#         self.numero_de_serie = numero_de_serie
#         self.instrucoes_de_armazenamento = instrucoes_de_armazenamento

#     def f_a_create_keys(self):
#         return {
#             "id": self.id,
#             "nome_do_produto": self.nome_do_produto,
#             "nome_da_empresa": self.nome_da_empresa,
#             "data_de_fabricacao": self.data_de_fabricacao,
#             "data_de_validade": self.data_de_validade,
#             "numero_de_serie": self.numero_de_serie,
#             "instrucoes_de_armazenamento": self.instrucoes_de_armazenamento,
#         }

