from Types import DataType


class CalcExcellent:
    def __init__(self, data: DataType) -> None:
        self.data = data

    def calc(self) -> int:
        excellent_count = 0
        for subjects in self.data.values():
            if all(score >= 90 for _, score in subjects):
                excellent_count += 1
        return excellent_count