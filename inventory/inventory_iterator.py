from collections.abc import Iterator, Iterable


class InventoryIterator(Iterator):
    def __init__(self, iterable):
        self._iterable = iterable
        self._position = 0

    def __next__(self):
        """Retorna o próximo elemento da coleção.

        Uma exceção é lançada quando não há mais elementos a serem percorridos.
        """
        try:
            current_value = self._iterable[self._position]
        except IndexError:
            raise StopIteration()
        else:
            self._position += 1
            return current_value


class StockInventory(Iterable):
    def __init__(self):
        self._reports = []

    def add_report(self, report):
        self._reports.append(report)

    def __iter__(self):
        """Retorna o iterador a partir da coleção de livros em estoque.

        Equivalente ao método iterator "ConcreteAgreggator" do diagrama.
        """
        return InventoryIterator(self._reports)
