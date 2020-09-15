from datetime import datetime
from collections import Counter
from reports.simple_report import SimpleReport


class CompleteReport:
    def __init__(self, list_os_dicts):
        self.list_os_dicts = list_os_dicts
        self.module_date = "%Y-%m-%d"
    def generate(self):
        simple_return = SimpleReport.generate(self.list_os_dicts)
