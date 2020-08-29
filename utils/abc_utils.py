from utils.abc_utils_abstract import (
    I_Factory_Report,
    I_Factory_Report_Complete,
)


class Format_Report_Simple(I_Factory_Report):
    def __init__(self, fabricacao, validade, nome_da_empresa):
        self.fabricacao = fabricacao
        self.validade = validade
        self.nome_da_empresa = nome_da_empresa

    def f_deliver_formatted_report(self):
        report_simple = f"""
            Data de fabricação mais antiga → {self.fabricacao}
            Data de validade mais próxima → {self.validade}
            Empresa com maior quantidade
            de produtos estocados → {self.nome_da_empresa}
            """
        return report_simple


class Format_Report_Complete(I_Factory_Report_Complete):
    @staticmethod
    def f_deliver_formatted_report(classe_report_simple, counter):
        str_report_return = f"""\033[1;32m
        {classe_report_simple}
        \n
        Produtos estocados por empresa:
        \033[1;35m
        """
        for inc, amount in counter.items():
            reports = f" - {inc}: {amount}"
            str_report_return += f"\033[1;35m{reports}\n"
        return str_report_return
