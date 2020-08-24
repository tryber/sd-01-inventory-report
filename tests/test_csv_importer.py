from importer.csv_importer import sum_plus


def test_sum_plus_10_sum_10_equal_20():
    reality = sum_plus(10, 10)
    expectancy = 20
    assert reality == expectancy
