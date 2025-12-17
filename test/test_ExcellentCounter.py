from src.Types import DataType
from src.ExcellentCounter import ExcellentCounter
import pytest


class TestExcellentCounter:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, int]:
        data: DataType = {
            "Студент1": [("математика", 90), ("физика", 95)],
            "Студент2": [("математика", 85), ("физика", 90)],
            "Студент3": [("математика", 100), ("физика", 100)]
        }
        expected_count = 2  # Студент1 и Студент3
        return data, expected_count

    def test_count(self, input_data: tuple[DataType, int]) -> None:
        counter = ExcellentCounter(input_data[0])
        assert counter.count() == input_data[1]
