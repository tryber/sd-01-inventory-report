from reports.simple_report import SimpleReport

from reports.complete_report import CompleteReport

from importer.importer import ABC, abstractmethod


# class Inventory(ABC):
#     @abstractmethod
#     def f_import():
#         """implementação da classe abstrata"""


# class CsvImporter(Inventory):
#     def __init__(self, flag=None, data=None):
#         self.simple = SimpleReport()
#         self.complete = CompleteReport()
#         self.flag = flag or "simple"
#         self.data = data or []

#     def f_import(self, flag, data):
#         if flag == "simple":
#             return self.simple.f_generate(data)
#         return self.complete.f_generate(data)


# class JsonImporter(Inventory):
#     def __init__(self, flag=None, data=None):
#         self.simple = SimpleReport()
#         self.complete = CompleteReport()
#         self.flag = flag or "simple"
#         self.data = data or []

#     def f_import(self, flag, data):
#         if flag == "simple":
#             return self.simple.f_generate(data)
#         return self.complete.f_generate(data)


# class XmlImporter(Inventory):
#     def __init__(self, flag=None, data=None):
#         self.simple = SimpleReport()
#         self.complete = CompleteReport()
#         self.flag = flag or "simple"
#         self.data = data or []

#     def f_import(self, flag, data):
#         if flag == "simple":
#             return self.simple.f_generate(data)
#         return self.complete.f_generate(data)


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
