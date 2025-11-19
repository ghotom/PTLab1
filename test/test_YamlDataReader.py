import pytest
from src.Types import DataType
from src.YamlDataReader import YamlDataReader


class TestYamlDataReader:
    @pytest.fixture
    def file_content(self) -> tuple[str, DataType]:
        text = """
Иванов Иван Иванович:
  математика: 95
  литература: 92
  программирование: 100
Петров Пётр Петрович:
  математика: 70
  химия: 85
        """
        data = {
            "Иванов Иван Иванович": [
                ("математика", 95),
                ("литература", 92),
                ("программирование", 100)
            ],
            "Петров Пётр Петрович": [
                ("математика", 70),
                ("химия", 85)
            ]
        }
        return text, data

    @pytest.fixture
    def filepath(self, file_content, tmp_path) -> str:
        p = tmp_path / "data.yaml"
        p.write_text(file_content[0].strip(), encoding="utf-8")
        return str(p)

    def test_read(self, filepath, file_content):
        reader = YamlDataReader()
        result = reader.read(filepath)
        assert result == file_content[1]
