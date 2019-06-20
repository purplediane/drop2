"""Remove from io import open"""
from lib2to3 import fixer_base
from lib2to3.fixer_util import BlankLine


class FixOpen(fixer_base.BaseFix):
    BM_compatible = True

    PATTERN = r"""
        simple_stmt< import_from< 'from' 'io' 'import' 'open' > '\n' >
    """

    def transform(self, node, results):
        new = BlankLine()
        new.prefix = node.prefix
        return new
