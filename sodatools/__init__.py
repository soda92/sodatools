from pathlib import Path
from contextlib import contextmanager
import os
import glob


@contextmanager
def CD(d: str):
    old = os.getcwd()
    os.chdir(d)
    yield
    os.chdir(old)


def read_path(p: Path) -> str:
    return p.read_text(encoding="utf8")


def write_path(p: Path, content: str) -> None:
    p.write_text(content, encoding="utf8")


def str_path(p: Path) -> str:
    return str(p).replace("\\", "/")


def get_glob_files(*patterns, recursive=True, root_dir=".") -> list[Path]:
    ret = []
    if root_dir == ".":
        root_dir = os.getcwd()
    root_dir = Path(root_dir).resolve()
    for pattern in patterns:
        files = glob.glob(pattern, recursive=True, root_dir=str_path(root_dir))
        files = map(root_dir.joinpath, files)
        ret.extend(files)
    return ret


__all__ = ["read_path", "write_path", "str_path", "CD", "get_glob_files"]
