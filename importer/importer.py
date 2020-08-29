from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    def f_import_data(self, path):
        """
        implementação da classe abstrata Importer
        Aqui vamos usar o designer partners Strategy
        """
