from reports.simple_report import SimpleReport

from utils.abc_utils import Format_Report_Complete

from collections import Counter


class CompleteReport(SimpleReport):
    def f_generate(self, array):

        report_simple = super().f_generate(array)
        counter = Counter(empresa["nome_da_empresa"] for empresa in array)
        print(report_simple)
        print("Produtos estocados por empresa:")
        str_report_return = ""
        for inc, amount in counter.items():
            reports = Format_Report_Complete.f_deliver_formatted_report(inc, amount)
            str_report_return += f"\033[1;35m{reports}\n"

        return str_report_return
