from lib2to3.fixes.fix_future import FixFuture as BaseFixFuture


class FixFuture(BaseFixFuture):
    PATTERN = r"""
        simple_stmt< {pattern} '\n' >
    """.format(pattern=BaseFixFuture.PATTERN)
