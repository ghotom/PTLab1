import yaml
from Types import DataType
from DataReader import DataReader


class YamlDataReader(DataReader):

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            raw_data = yaml.safe_load(file)
        students: DataType = {}
        for item in raw_data:
            name = list(item.keys())[0]
            subjects = item[name]
            students[name] = [(subj, int(score)) for subj,
                               score in subjects.items()]
        return students
