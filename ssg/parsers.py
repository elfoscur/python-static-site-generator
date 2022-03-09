from typing import List
from pathlib import Path

class Parser:
    extensions: List[str] = []

    def valid_extension(self, extension):
        return extension in self.extensions

    def parse(path, source, dest):
        path: Path
        source: Path
        dest: Path

        raise NotImplementedError


    def read(path):
        with (open(path, 'rt', 'utf-8')) as file:
            return file.read()
