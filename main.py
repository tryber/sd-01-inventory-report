from inventory.inventory import Inventory

from importer.xml_importer import XmlImporter

from importer.json_importer import JsonImporter

from importer.csv_importer import CsvImporter

from inventory.inventory_iterator import StockInventory

path = {
    "csv": "data/inventory_20200823.csv",
    "json": "data/inventory_20200823.json",
    "xml": "data/inventory_20200823.xml",
}


invetory_xml = Inventory(XmlImporter())
invetory_json = Inventory(JsonImporter())
invetory_csv = Inventory(CsvImporter())

stock_xml = invetory_xml.f_import_data("simple", path["xml"])
stock_json = invetory_json.f_import_data("simple", path["json"])
stock_csv = invetory_csv.f_import_data("simple", path["csv"])

stock = StockInventory()

stock.add_report(stock_xml)
stock.add_report(stock_json)
stock.add_report(stock_csv)

iterator = iter(stock)


print("*" * 70)
for report in stock:
    print(report)
print("*" * 70)


"""
Esse arquivo é somente de testes. não é nescessário fazer CR nele!!!

"""
