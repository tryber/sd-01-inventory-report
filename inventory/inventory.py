# from reports.complete_report import CompleteReport
from reports.simple_report import SimpleReport


class Inventory:
    def __init__(self, file_type):
        self.simple = SimpleReport
        # self.complete = CompleteReport()
        self.importer = file_type

    def import_data(self, coverage, path):
        data = self.importer.import_data(path)
        if coverage == "simples":
            return self.simple(data).generate()
        # return self.complete.generate(data)
