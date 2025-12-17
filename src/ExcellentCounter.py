from Types import DataType


class ExcellentCounter:

    def __init__(self, data: DataType) -> None:
        self.data = data

    def count(self) -> int:
        count = 0
        for subjects in self.data.values():
            if all(score >= 90 for _, score in subjects):
                count += 1
        return count
