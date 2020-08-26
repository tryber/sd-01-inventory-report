from reports.simple_report import SimpleReport

from reports.complete_report import CompleteReport


class Inventory:
    def __init__(self):
        self.simple = SimpleReport()
        self.complete = CompleteReport()

    def f_shows_reports(self, flag, data):
        if flag == "simple":
            return self.simple.f_generate(data)
        return self.complete.f_generate(data)
