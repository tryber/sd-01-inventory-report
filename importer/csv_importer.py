from csv import DictReader
from importer.importer import Importer


class CsvImporter(Importer):
    def import_data(path):
        if not path.endswith("csv"):
            raise ValueError("Arquivo invalido")
        data = []
        with open(path, "r", encoding='utf-8-sig') as csv_file:
            readCSV = DictReader(csv_file, delimiter=",")
            for values in readCSV:
                newDic = {key: values[key] for key in values}
                data.append(newDic)
        return data
