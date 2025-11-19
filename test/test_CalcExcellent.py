import pytest
from src.Types import DataType
from src.CalcExcellent import CalcExcellent


class TestCalcExcellent:
    @pytest.fixture
    def sample_data(self) -> DataType:
        return {
            "Иванов Иван": [("мат", 95), ("прог", 98), ("лит", 92)],
            "Петров Петр": [("мат", 100), ("хим", 88)],
            "Сидоров Алексей": [("мат", 90), ("физ", 91), ("рус", 95)],
            "Козлов Дмитрий": [("мат", 85), ("прог", 79)]
        }

    def test_calc_excellent(self, sample_data):
        calc = CalcExcellent(sample_data)
        assert calc.calc() == 2