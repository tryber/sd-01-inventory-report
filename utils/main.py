from abc import ABCMeta, abstractclassmethod


class I_Factory(metaclass=ABCMeta):
    @abstractclassmethod
    def f_a_create_keys():
        """ the create keys """


class Keys_By_create(I_Factory):
    def __init__(
        self,
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    ):
        self.id = id
        self.nome_do_produto = nome_do_produto
        self.nome_da_empresa = nome_da_empresa
        self.data_de_fabricacao = data_de_fabricacao
        self.data_de_validade = data_de_validade
        self.numero_de_serie = numero_de_serie
        self.instrucoes_de_armazenamento = instrucoes_de_armazenamento

    def f_a_create_keys(self):
        return {
            "id": self.id,
            "nome_do_produto": self.nome_do_produto,
            "nome_da_empresa": self.nome_da_empresa,
            "data_de_fabricacao": self.data_de_fabricacao,
            "data_de_validade": self.data_de_validade,
            "numero_de_serie": self.numero_de_serie,
            "instrucoes_de_armazenamento": self.instrucoes_de_armazenamento,
        }
