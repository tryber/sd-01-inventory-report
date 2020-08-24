from utils.main import Keys_By_create

import pandas as pd


class SimpleReport(Keys_By_create):
    def __init__(self, list_of_dicts=None):
        self.list_of_dicts = list_of_dicts or list()

    def f_generate(self):
        file_json = pd.read_json("data/inventory_20200823.json")
        return file_json

