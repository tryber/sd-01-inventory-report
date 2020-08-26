from reports.simple_report import SimpleReport

from reports.complete_report import CompleteReport

from utils.abc_utils import GetData

import json

path = {
    "csv": "data/inventory_20200823.csv",
    "json": "data/inventory_20200823.json",
    "xml": "data/inventory_20200823.xml",
}

data_raw = GetData(path["xml"])

data = data_raw.f_by_scrap_data_xml()

# report_simple = SimpleReport()

# new_report_simple = report_simple.f_generate(data)


# report = CompleteReport()

# new_report = report.f_generate(data)

print("*" * 70)
print(data)

print("*" * 70)
