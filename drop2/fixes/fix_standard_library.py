"""Fixer for future.standard_librayr"""
from lib2to3 import fixer_base
from lib2to3.fixer_util import BlankLine

class FixStandardLibrary(fixer_base.BaseFix):
    BM_compatible = True

    PATTERN = r"""
        simple_stmt<
            power<
                'standard_library' trailer< '.' 'install_aliases' >
                trailer< '(' ')' >
            >
            '\n'
        >
        |
        simple_stmt<
            import_from< 'from' 'future' 'import' 'standard_library' >
            '\n'
        >
      """

    def transform(self, node, results):
        new = BlankLine()
        new.prefix = node.prefix
        return new
