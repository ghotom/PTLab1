import argparse
import sys
from pathlib import Path

from CalcRating import CalcRating
from TextDataReader import TextDataReader
from YamlDataReader import YamlDataReader
from CalcExcellent import CalcExcellent


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def create_reader(path: str):
    suffix = Path(path).suffix.lower()
    if suffix in {".yaml", ".yml"}:
        return YamlDataReader()
    else:
        return TextDataReader()


def main():
    path = get_path_from_arguments(sys.argv[1:])

    reader = create_reader(path)
    students = reader.read(path)
    print("Students:", students)

    rating = CalcRating(students).calc()
    print("Rating:", rating)

    excellent_count = CalcExcellent(students).calc()
    print(f"Количество студентов-отличников: {excellent_count}")


if __name__ == "__main__":
    main()
