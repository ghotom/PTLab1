import yaml
from Types import DataType
from DataReader import DataReader


class YamlDataReader(DataReader):
    def read(self, path: str) -> DataType:
        with open(path, encoding="utf-8") as file:
            raw_data = yaml.safe_load(file)

        students: DataType = {}
        for student_name, subjects in raw_data.items():
            students[student_name] = []
            for subject, score in subjects.items():
                students[student_name].append((subject, int(score)))
        return students