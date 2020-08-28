from inventory.inventory import Inventory

from importer.xml_importer import XmlImporter

from importer.json_importer import JsonImporter

path = {
    "csv": "data/inventory_20200823.csv",
    "json": "data/inventory_20200823.json",
    "xml": "data/inventory_20200823.xml",
}


testes_invetory = Inventory(XmlImporter())


# print("*" * 70)
# print(testes_invetory.f_import_data("complete", path["xml"]))
# print("*" * 70)

testes_invetory.importer = JsonImporter()

print("*" * 70)
print(testes_invetory.f_import_data("complete", path["csv"]))
print("*" * 70)


"""
Esse arquivo é somente de testes. não é nescessário fazer CR nele!!!

"""
