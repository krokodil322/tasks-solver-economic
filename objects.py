import constants

from collections import namedtuple


# объект описывающий основных рабочих
BasicWorker = namedtuple('BasicWorker', ('title', 'quan', 'tariff_rate'))
# объект описывающий вспомогательных рабочих
AuxiliaryWorker = namedtuple('AuxiliaryWorker', ('title', 'quan', 'tariff_rate'))
# объект описывающий итр
ETWorker = namedtuple('ETWorker', ('title', 'quan', 'salary'))

# объект для работы с рабочими как с единым целым
Worker = namedtuple('Worker', ('basic_worker', 'auxiliary_worker', 'et_worker'))

class Formula:
    """
    Для работы с формулами и их значениями
    """
    def __init__(self, workers: tuple):
        # кортеж с объектами описывающих работников
        self.workers = workers
        # число рабочих
        self.quan_workers = sum(worker.quan for worker in workers)

        # Сср.чт - среднечасовая тарифная ставка
        self.hourly_rate = 0
        # Зтар - тарифная оплата труда
        self.tariff_salary = 0
        # Дн - доплата за работу в ночное время
        self.surch_night_time = 0

    def calc_hourly_rate(self) -> None:
        """
        Вычисляет среднечасовую тарифную ставку по бригаде = Сср.чт
        """
        result = sum(worker.quan * worker.tariff_rate for worker in self.workers)
        self.hourly_rate = round(result / self.quan_workers, 2)

    def calc_tariff_salary(self) -> None:
        """
        Вычисляет тарифную оплату труда = Зтар
        """
        self.tariff_salary = round(self.hourly_rate * constants.EWT * self.quan_workers, 2)

    def calc_surch_night_time(self) -> None:
        """
        Вычисляет доплату за работу в ночное время = Дн
        """
        self.surch_night_time = round(self.hourly_rate * self.quan_workers * constants.NH * 0.4, 2)

