from importer.importer import Importer

from json import load


class JsonImporter(Importer):
    def import_data(self, path):
        if not path.endswith("json"):
            raise ValueError("Arquivo invalido")
        data = []
        with open(path) as file:
            value = load(file)
            for values in value:
                data.append(values)
        return data
