from objects import *
from constants import *

from unittest import TestCase, main


class FormulaObjectTest(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.workers = Worker(
            basic_worker=(
                BasicWorker('Оператор по ДНГ', 6, 66.2),
                BasicWorker('Оператор по ДНГ', 8, 68.7),
                BasicWorker('Оператор по ДНГ', 8, 69.9),
            ),
            auxiliary_worker=(
                AuxiliaryWorker('Слесарь', 2, 54.7),
                AuxiliaryWorker('Сварщик', 3, 54.9),
            ),
            et_worker=(
                ETWorker('Мастер', 1, 41500)
            )
        )
        self.formulas = Formula(self.workers.basic_worker)

    def test_calc_hourly_rate(self):
        self.formulas.calc_hourly_rate()
        self.assertTrue(self.formulas.hourly_rate == 68.45)

    def test_calc_tariff_salary(self):
        self.formulas.calc_hourly_rate()
        self.formulas.calc_tariff_salary()
        self.assertTrue(self.formulas.tariff_salary == 2334145.0)

    def test_calc_surch_night_time(self):
        self.formulas.calc_hourly_rate()
        print(self.formulas.surch_night_time)




if __name__ == '__main__':
    main()