from reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __init__(self):
        pass

    @staticmethod
    def f_generate():
        instan_herdade = SimpleReport()
        lista = instan_herdade.f_generate()
        return lista
