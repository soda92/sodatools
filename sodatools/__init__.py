from pathlib import Path
from contextlib import contextmanager
import os


@contextmanager
def CD(d: str):
    old = os.getcwd()
    os.chdir(d)
    yield
    os.chdir(old)


def read_path(p: Path) -> str:
    return p.read_text(encoding="utf8")


def write_path(p: Path, content: str):
    p.write_text(content, encoding="utf8")


def str_path(p: Path):
    return str(p).replace("\\", "/")


__all__ = ["read_path", "write_path", "str_path", "CD"]
