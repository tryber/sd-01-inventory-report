from reports.simple_report import SimpleReport

from reports.complete_report import CompleteReport


class Inventory(SimpleReport, CompleteReport):
    def __init__(self, flag):
        self.flag = flag

    def f_shows_reports(self):
        
