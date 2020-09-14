from importer.importer import Importer

from csv import DictReader


class CsvImporter(Importer):
    def import_data(self, path):
        if not path.endswith("csv"):
            raise ValueError("Arquivo invalido")
        data = []
        with open(path, "r", encoding='utf-8-sig') as csv_file:
            readCSV = DictReader(csv_file, delimiter=",")
            for values in readCSV:
                data.append({key: values[key] for key in values})
        return data

