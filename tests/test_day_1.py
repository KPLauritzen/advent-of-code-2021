from src.utils import DataLoader
from pathlib import Path

def test_day_1_part_1():
    from src.day_1 import part_1
    dl = DataLoader(file_path=Path("data/day_1_test_input.txt"))
    dl.transform_to_int()
    test_input = dl.data

    assert part_1(test_input) == 7



def test_day1_part_2():
    from src.day_1 import part_2
    dl = DataLoader(file_path=Path("data/day_1_test_input.txt"))
    dl.transform_to_int()
    test_input = dl.data

    assert part_2(test_input) == 5