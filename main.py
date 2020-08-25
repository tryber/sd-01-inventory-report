from reports.simple_report import SimpleReport

from reports.complete_report import CompleteReport

from utils.abc_utils import GetData


json_retriever = GetData("data/inventory_20200823.json")

data = json_retriever.f_by_get_data_json()

report_simple = SimpleReport()

new_report_simple = report_simple.f_generate(data)


report = CompleteReport()

new_report = report.f_generate(data)

print("*" * 70)

print(new_report)

print("*" * 70)
