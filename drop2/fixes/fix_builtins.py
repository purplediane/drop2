"""
Remove builtins imports

from builtins import foo is replaced with an empty line.

"""
from lib2to3 import fixer_base
from lib2to3.fixer_util import BlankLine


class FixBuiltins(fixer_base.BaseFix):
    BM_compatible = True

    PATTERN = r"""
        simple_stmt< import_from< 'from' 'builtins' 'import' any > '\n' >
        |
        simple_stmt<
            import_from<
                'from' dotted_name<'future' '.' 'builtins'> 'import' any
            >
            '\n'
        >
    """

    def transform(self, node, results):
        new = BlankLine()
        new.prefix = node.prefix
        return new
