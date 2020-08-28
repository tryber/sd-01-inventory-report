from reports.simple_report import SimpleReport

from reports.complete_report import CompleteReport


class Inventory:
    def __init__(self, import_strategy):
        self.simple = SimpleReport()
        self.complete = CompleteReport()
        self.importer = import_strategy

    def f_import_data(self, flag, path):
        data = self.importer.f_import_data(path)
        if flag == "simple":
            return self.simple.f_generate(data)
        return self.complete.f_generate(data)
