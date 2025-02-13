from pathlib import Path


def read_path(p: Path) -> str:
    return p.read_text(encoding="utf8")


def write_path(p: Path, content: str):
    p.write_text(content, encoding="utf8")


def str_path(p: Path):
    return str(p).replace("\\", "/")


__all__ = ["read_path", "write_path", "str_path"]
