import json
from importer.importer import Importer


class JsonImporter(Importer):
    def import_data(path):
        if not path.endswith("json"):
            raise ValueError("Arquivo invalido")
        list_of_dicts = []
        with open(path) as file:
            file_load = json.load(file)
            for row in file_load:
                list_of_dicts.append(row)
        return list_of_dicts
