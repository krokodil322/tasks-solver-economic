from objects import *
from constants import *

from unittest import TestCase, main


# workers = Worker(
#     basic_worker=(
#         BasicWorker('Оператор по ДНГ', 6, 66.2),
#         BasicWorker('Оператор по ДНГ', 8, 68.7),
#         BasicWorker('Оператор по ДНГ', 8, 69.9),
#     ),
#     auxiliary_worker=(
#         AuxiliaryWorker('Слесарь', 2, 54.7),
#         AuxiliaryWorker('Сварщик', 3, 54.9),
#     ),
#     et_worker=(
#         ETWorker('Мастер', 1, 41500)
#     )
# )

class TestFormulaByBasicWorker(TestCase):
    """Тест класса Formula по расчёту основных рабочих"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        workers = (
            BasicWorker('Оператор по ДНГ', 6, 66.2),
            BasicWorker('Оператор по ДНГ', 8, 68.7),
            BasicWorker('Оператор по ДНГ', 8, 69.9),
        )
        self.formulas = Formula(workers=workers)

    def test_calc_hourly_rate(self):
        self.formulas.calc_hourly_rate()
        self.assertTrue(self.formulas.hourly_rate == 68.45)

    def test_calc_tariff_salary(self):
        self.formulas.calc_hourly_rate()
        self.formulas.calc_tariff_salary()
        self.assertTrue(self.formulas.tariff_salary == 2334145.0)

    def test_calc_surch_night_time(self):
        self.formulas.calc_hourly_rate()
        self.formulas.calc_surch_night_time()
        self.assertTrue(self.formulas.surch_night_time == 49284.0)

    def test_calc_surch_extended_zone(self):
        self.formulas.calc_hourly_rate()
        self.formulas.calc_surch_extended_zone()
        self.assertTrue(self.formulas.surch_extended_zone == 466829.0)

    def test_calc_surch_public_holidays(self):
        self.formulas.calc_hourly_rate()
        self.formulas.calc_surch_public_holidays()
        self.assertTrue(self.formulas.surch_public_holidays == 28338.3)

    def test_calc_surch_work_experience(self):
        self.formulas.calc_hourly_rate()
        self.formulas.calc_tariff_salary()
        self.formulas.calc_surch_work_experience()
        self.assertTrue(self.formulas.surch_work_experience == 536853.35)

    def test_calc_amount_surchs(self):
        self.formulas.calc_hourly_rate()
        self.formulas.calc_tariff_salary()
        self.formulas.calc_surch_night_time()
        self.formulas.calc_surch_extended_zone()
        self.formulas.calc_surch_public_holidays()
        self.formulas.calc_surch_work_experience()
        self.formulas.calc_amount_surchs()
        self.assertTrue(self.formulas.amount_surchs == 1081304.65)

    def test_calc_direct_wages(self):
        self.formulas.calc_hourly_rate()
        self.formulas.calc_tariff_salary()
        self.formulas.calc_surch_night_time()
        self.formulas.calc_surch_extended_zone()
        self.formulas.calc_surch_public_holidays()
        self.formulas.calc_surch_work_experience()
        self.formulas.calc_amount_surchs()
        self.formulas.calc_direct_wages()
        self.assertTrue(self.formulas.direct_wages == 3415449.65)

    def test_calc_amount_premium(self):
        self.formulas.calc_hourly_rate()
        self.formulas.calc_tariff_salary()
        self.formulas.calc_surch_night_time()
        self.formulas.calc_surch_extended_zone()
        self.formulas.calc_surch_public_holidays()
        self.formulas.calc_surch_work_experience()
        self.formulas.calc_amount_surchs()
        self.formulas.calc_direct_wages()
        self.formulas.calc_amount_premium()
        self.assertTrue(self.formulas.amount_premium == 2049269.79)

    def test_calc_amount_surchs_DC(self):
        self.formulas.calc_hourly_rate()
        self.formulas.calc_tariff_salary()
        self.formulas.calc_surch_night_time()
        self.formulas.calc_surch_extended_zone()
        self.formulas.calc_surch_public_holidays()
        self.formulas.calc_surch_work_experience()
        self.formulas.calc_amount_surchs()
        self.formulas.calc_direct_wages()
        self.formulas.calc_amount_premium()
        self.formulas.calc_amount_surchs_DC()
        self.assertTrue(self.formulas.amount_surchs_DC == 3825303.61)

    def test_calc_amount_surchs_NA(self):
        self.formulas.calc_hourly_rate()
        self.formulas.calc_tariff_salary()
        self.formulas.calc_surch_night_time()
        self.formulas.calc_surch_extended_zone()
        self.formulas.calc_surch_public_holidays()
        self.formulas.calc_surch_work_experience()
        self.formulas.calc_amount_surchs()
        self.formulas.calc_direct_wages()
        self.formulas.calc_amount_premium()
        self.formulas.calc_amount_surchs_NA()
        self.assertTrue(self.formulas.amount_surchs_NA == 4371775.55)

    def test_calc_basic_salary(self):
        self.formulas.calc_hourly_rate()
        self.formulas.calc_tariff_salary()
        self.formulas.calc_surch_night_time()
        self.formulas.calc_surch_extended_zone()
        self.formulas.calc_surch_public_holidays()
        self.formulas.calc_surch_work_experience()
        self.formulas.calc_amount_surchs()
        self.formulas.calc_direct_wages()
        self.formulas.calc_amount_premium()
        self.formulas.calc_amount_surchs_DC()
        self.formulas.calc_amount_surchs_NA()
        self.formulas.calc_basic_salary()
        self.assertTrue(self.formulas.basic_salary == 13661798.6)

    def test_calc_additional_salary(self):
        self.formulas.calc_hourly_rate()
        self.formulas.calc_tariff_salary()
        self.formulas.calc_surch_night_time()
        self.formulas.calc_surch_extended_zone()
        self.formulas.calc_surch_public_holidays()
        self.formulas.calc_surch_work_experience()
        self.formulas.calc_amount_surchs()
        self.formulas.calc_direct_wages()
        self.formulas.calc_amount_premium()
        self.formulas.calc_amount_surchs_DC()
        self.formulas.calc_amount_surchs_NA()
        self.formulas.calc_basic_salary()
        self.formulas.calc_additional_salary()
        self.assertTrue(self.formulas.additional_salary == 2459123.75)

    def test_calc_total_salary(self):
        self.formulas.calc_hourly_rate()
        self.formulas.calc_tariff_salary()
        self.formulas.calc_surch_night_time()
        self.formulas.calc_surch_extended_zone()
        self.formulas.calc_surch_public_holidays()
        self.formulas.calc_surch_work_experience()
        self.formulas.calc_amount_surchs()
        self.formulas.calc_direct_wages()
        self.formulas.calc_amount_premium()
        self.formulas.calc_amount_surchs_DC()
        self.formulas.calc_amount_surchs_NA()
        self.formulas.calc_basic_salary()
        self.formulas.calc_additional_salary()
        self.formulas.calc_total_salary()
        self.assertTrue(self.formulas.total_salary == 16120922.35)

    def test_calc_amount_salary(self):
        self.formulas.calc_hourly_rate()
        self.formulas.calc_tariff_salary()
        self.formulas.calc_surch_night_time()
        self.formulas.calc_surch_extended_zone()
        self.formulas.calc_surch_public_holidays()
        self.formulas.calc_surch_work_experience()
        self.formulas.calc_amount_surchs()
        self.formulas.calc_direct_wages()
        self.formulas.calc_amount_premium()
        self.formulas.calc_amount_surchs_DC()
        self.formulas.calc_amount_surchs_NA()
        self.formulas.calc_basic_salary()
        self.formulas.calc_additional_salary()
        self.formulas.calc_total_salary()
        self.formulas.calc_amount_salary()
        self.assertTrue(self.formulas.amount_salary == 61064.1)


class TestFormulaByAuxiliaryWorker(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        workers = (
            AuxiliaryWorker('Слесарь', 2, 54.7),
            AuxiliaryWorker('Сварщик', 3, 54.9),
        )
        self.formulas = Formula(workers=workers)

    


if __name__ == '__main__':
    main()