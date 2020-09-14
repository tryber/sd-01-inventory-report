from importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(self, path):
        if not path.endswith("xml"):
            raise ValueError("Arquivo invalido")
        data = []
        tree = ET.parse(path)
        root = tree.getroot()

        for elem in root.iter('record'):
            obj = {}
            for elem2 in elem.iter():
                obj[elem2.tag] = elem2.text
            data.append(obj)
        return data
