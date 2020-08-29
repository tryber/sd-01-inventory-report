from importer.importer import Importer

from csv import DictReader


class CsvImporter(Importer):
    def f_import_data(self, path):
        if not path.endswith("csv"):
            raise ValueError("\033[1;31minvalid file extension")
        data = []
        with open(path, "r") as file_csv:
            rd = DictReader(file_csv, delimiter=",")
            for arq in rd:
                data.append(arq)
        return data
