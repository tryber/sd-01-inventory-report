from importer.importer import Importer

from json import load


class JsonImporter(Importer):
    def f_import_data(self, path):
        if not path.endswith("json"):
            raise ValueError("\033[1;31minvalid file extension")
        data = []
        with open(path) as file:
            obj = load(file)
            for arq in obj:
                data.append(arq)
        return data
