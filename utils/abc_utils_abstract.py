from abc import ABC, abstractmethod


class I_Factory_Report(ABC):
    @abstractmethod
    def f_deliver_formatted_report():
        """ entrega as keys do objeto de output """


class I_Factory_Report_Complete(ABC):
    @abstractmethod
    def f_deliver_formatted_report():
        """ entrega as keys do objeto de output """

