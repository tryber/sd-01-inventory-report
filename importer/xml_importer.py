from importer.importer import Importer

from bs4 import BeautifulSoup as bf


class XmlImporter(Importer):
    def f_import_data(self, path):
        if not path.endswith("xml"):
            raise ValueError("\033[1;31minvalid file extension")
        try:
            file_xml = open(path)
            soup = bf(file_xml, "html.parser")
            records = [
                {field.name: field.text for field in record.contents}
                for record in soup.find_all("record")
            ]
            return records
        except Exception as exc:
            return exc
