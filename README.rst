drop2
=====

This is a command-line program which can be used to clean up futurize-upgraded code that no longer needs to support Python 2.

This program is uses ``lib2to3`` in the Python standard library and all command-line arguments accepted by ``2to3`` also work with ``drop2``.


Example
-------

Given this file, ``greet.py``:

.. code-block:: python

    from __future__ import print_function
    from builtins import input
    from future import standard_library
    standard_library.install_aliases()
    name = input("What's your name? ")
    print("Hello {name}".format(name=name))

Running ``drop2`` will produce the following output:

.. code-block:: diff

    $ python drop2 greet.py
    RefactoringTool: Refactored greet.py
    --- greet.py    (original)
    +++ greet.py    (refactored)
    @@ -1,6 +1,2 @@
    -from __future__ import print_function
    -from builtins import input
    -from future import standard_library
    -standard_library.install_aliases()
     name = input("What's your name? ")
      print("Hello {name}".format(name=name))
    RefactoringTool: Files that need to be modified:
    RefactoringTool: greet.py

To fix the given files in-place, use the ``-w`` argument (just as with ``futurize``).


Fixes
-----

The available fixers can be seen with ``-l``:

.. code-block:: bash

    $ python drop2 -l
    Available transformations for the -f/--fix option:
    builtins
    future
    open
    past
    standard_library

All of these fixes are enabled by default.

Each of these fixes briefly explained:

- builtins: remove ``from builtins import ...`` lines
- future: remove ``from __future__ import ...`` lines (based on the same fixer in ``2to3``)
- open: remove ``from io import open`` line
- past: remove ``from past.* import ...`` lines.
- standard_library: remove ``from future import standard_library`` and ``standard_library.install_aliases()``

To run just particular fixes, use the ``-f`` argument.
To exclude particular fixes, use the ``-x`` argument.


License
-------

This code is provided under the `MIT License <https://th.mit-license.org>`_.
