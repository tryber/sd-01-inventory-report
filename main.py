from inventory.inventory import Inventory
from importer.json_importer import JsonImporter
# invetory_xml = Inventory(XmlImporter())
invetory_json = Inventory(JsonImporter()).import_data('simples', 'data/inventory_20200823.json')
# invetory_csv = Inventory(CsvImporter())
