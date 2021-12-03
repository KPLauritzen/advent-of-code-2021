from __future__ import annotations

from pathlib import  Path
from typing import List, Any

class DataLoader:

    def __init__(self, file_path: Path):
        self.data = self._load_input_file(file_path)

    def _load_input_file(self, file_path: Path) -> List[Any]:
        with open(file_path) as f:
            return f.readlines()

    def transform_to_int(self) -> DataLoader:
        self.data = [int(x) for x in self.data]
        return self

