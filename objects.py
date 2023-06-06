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
    """Для работы с формулами и их значениями"""
    def __init__(self, workers: tuple):
        # кортеж с объектами описывающих работников
        self.workers = workers
        # общее число рабочих
        self.quan_workers = sum(worker.quan for worker in workers)

        # Сср.чт - среднечасовая тарифная ставка
        self.hourly_rate = None
        # Зтар - тарифная оплата труда
        self.tariff_salary = None
        # Дн - доплата за работу в ночное время
        self.surch_night_time = None
        # Др.з. - доплата за работу по расширенной зоне
        self.surch_extended_zone = None
        # Дпр.в - доплата за работу в праздничные и выходные дни
        self.surch_public_holidays = None
        # Дст.р. - доплата за стаж работы
        self.surch_work_experience = None
        # Д - сумма всех доплат
        self.amount_surchs = None
        # Зпр - прямая оплата труда
        self.direct_wages = None
        # Пр - сумма премий
        self.amount_premium = None
        # РК - сумма доплат по районному коэффициенту
        self.amount_surchs_DC = None
        # СН - северная надбавка
        self.amount_surchs_NA = None
        # Зосн - основная оплата труда
        self.basic_salary = None
        # Здоп - дополнительная оплата труда
        self.additional_salary = None
        # Зобщ - общая оплата труда
        self.total_salary = None
        # Зср.м - среднемесячная зарплата
        self.amount_salary = None

    def calc_hourly_rate(self) -> None:
        """Вычисляет среднечасовую тарифную ставку по бригаде = Сср.чт"""
        result = sum(worker.quan * worker.tariff_rate for worker in self.workers)
        self.hourly_rate = round(result / self.quan_workers, 2)

    def calc_tariff_salary(self) -> None:
        """Вычисляет тарифную оплату труда = Зтар"""
        self.tariff_salary = round(self.hourly_rate * constants.EWT * self.quan_workers, 2)

    def calc_surch_night_time(self) -> None:
        """Вычисляет доплату за работу в ночное время = Дн"""
        self.surch_night_time = round(self.hourly_rate * constants.QWNT * constants.NH * 0.4, 2)

    def calc_surch_extended_zone(self) -> None:
        """Вычисляет доплату за работу по расширенной зоне = Др.з."""
        self.surch_extended_zone = round(self.hourly_rate * self.quan_workers * constants.EWT * constants.EAS, 2)

    def calc_surch_public_holidays(self) -> None:
        """Вычисляет доплату за работу в праздничные и выходные дни = Дпр.в"""
        self.surch_public_holidays = round(self.hourly_rate * constants.QWPH * constants.PH, 2)

    def calc_surch_work_experience(self) -> None:
        """Вычисляет доплату за стаж работы = Дст.р."""
        self.surch_work_experience = round(constants.WEA * self.tariff_salary, 2)

    def calc_amount_surchs(self) -> None:
        """Вычисляет сумму всех доплат = Д"""
        self.amount_surchs = round(
            self.surch_night_time + self.surch_extended_zone + \
            self.surch_public_holidays + self.surch_work_experience, 2
        )

    def calc_direct_wages(self) -> None:
        """Вычисляет прямую оплату труда = Зпр"""
        self.direct_wages = round(self.tariff_salary + self.amount_surchs, 2)

    def calc_amount_premium(self) -> None:
        """Вычисляет сумму премий = Пр"""
        self.amount_premium = round(self.direct_wages * constants.PP, 2)

    def calc_amount_surchs_DC(self) -> None:
        """Вычисляет сумму выплат по районному коэффициенту = РК"""
        self.amount_surchs_DC = round((self.direct_wages + self.amount_premium) * constants.DC, 2)

    def calc_amount_surchs_NA(self) -> None:
        """Вычисляет сумму выплат по северной надбавки = СН"""
        self.amount_surchs_NA = round((self.direct_wages + self.amount_premium) * constants.NA, 2)

    def calc_basic_salary(self) -> None:
        """Вычисляет основную оплату труда = Зосн"""
        self.basic_salary = round(
            self.direct_wages + self.amount_premium + \
            self.amount_surchs_DC + self.amount_surchs_NA, 2
        )

    def calc_additional_salary(self) -> None:
        """Вычисляет дополнительную оплату труда = Здоп"""
        self.additional_salary = round(self.basic_salary * constants.AS, 2)

    def calc_total_salary(self) -> None:
        """Вычисляет общую зарплату = Зобщ"""
        self.total_salary = round(self.basic_salary + self.additional_salary, 2)

    def calc_amount_salary(self) -> None:
        """Вычисляет среднемесячную зарплату = Зср.м"""
        self.amount_salary = round(self.total_salary / (12 * self.quan_workers), 2)