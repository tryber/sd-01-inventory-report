from reports.simple_report import SimpleReport

mock_data = [
    {
        "id": 1,
        "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2020-07-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
        "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus",
    }
]

mock_expectative = """
            Data de fabricação mais antiga → 2020-07-04
            Data de validade mais próxima → 2023-02-09
            Empresa com maior quantidade
            de produtos estocados → 1
            """


def test_class_SimpleReport_f_generate():
    report = SimpleReport()
    reality = report.f_generate(mock_data)
    expectancy = mock_expectative
    print("*" * 70)
    print(reality)
    print("*" * 70)
    assert reality == expectancy


def test_class_SimpleReport__f_date():
    from datetime import datetime

    report = SimpleReport()
    reality = report._f_date("2020-07-04")
    expectancy = datetime(2020, 7, 4).date()
    assert reality == expectancy
