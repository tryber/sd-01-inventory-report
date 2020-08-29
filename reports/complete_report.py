from reports.simple_report import SimpleReport

from utils.abc_utils import Format_Report_Complete

from collections import Counter


class CompleteReport(SimpleReport):
    def f_generate(self, data):
        report_simple = super().f_generate(data)
        counter = Counter(empresa["nome_da_empresa"] for empresa in data)
        reports = Format_Report_Complete.f_deliver_formatted_report(
            report_simple, counter
        )
        return reports
