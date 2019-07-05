from contextlib import contextmanager
from pathlib import Path
import pytest
from textwrap import dedent
from tempfile import NamedTemporaryFile
import sys

from drop2.main import main


def test_io_open_import_removed():
    INPUT = dedent("""
    import sys
    from io import open

    print(open(sys.argv[1]).read())
    """).strip()
    EXPECTED = dedent("""
    import sys

    print(open(sys.argv[1]).read())
    """).strip()
    with make_file(INPUT) as tmp_file:
        with patch_args(['-w', str(tmp_file)]):
            with pytest.raises(SystemExit):
                main()
        assert tmp_file.read_text() == EXPECTED


@contextmanager
def make_file(contents=None):
    """Context manager providing name of a file containing given contents."""
    with NamedTemporaryFile(mode='wt', encoding='utf-8', delete=False) as f:
        if contents:
            f.write(contents)
    path = Path(f.name)
    try:
        yield path
    finally:
        path.unlink()


@contextmanager
def patch_args(args=[]):
    """Context manager providing name of a file containing given contents."""
    old_args = sys.argv
    try:
        sys.argv = [old_args[0], *args]
        yield
    finally:
        sys.argv = old_args
