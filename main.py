from objects import *


workers = Worker(
    basic_worker=(
        BasicWorker('Слесарь', 2, 54.7), BasicWorker('Сварщик', 3, 54.9),
    ),
    auxiliary_worker=(
        AuxiliaryWorker('Оператор по ДНГ', 6, 66.2),
        AuxiliaryWorker('Оператор по ДНГ', 8, 68.7),
        AuxiliaryWorker('Оператор по ДНГ', 8, 69.9),
    ),
    et_worker=(
        ETWorker('Мастер', 1, 41500)
    )
)

formulas = Formula(workers.basic_worker)



