bloc-python
=================

.. image:: https://img.shields.io/pypi/v/bloc.svg
	:target: https://pypi.python.org/pypi/bloc

.. image:: https://img.shields.io/pypi/pyversions/bloc.svg
	:target: https://pypi.python.org/pypi/bloc

.. image:: https://img.shields.io/pypi/l/bloc.svg
	:target: https://pypi.python.org/pypi/bloc

.. image:: https://readthedocs.org/projects/bloc-python/badge/
    :target: http://bloc-python.readthedocs.io/en/latest/

A Python wrapper for the BLOC JSON-RPC API.

It integrates with `Walletd` and `BLOCd` and works with BLOC 3.0.

Example
-------

.. code-block:: python

    wallet.get_addresses()
    'abLoc....'
    {'id': 0, 'jsonrpc': '2.0', 'result': {'addresses': ['abLoc....']}}

    wallet.get_balance()
    {'id': 0, 'jsonrpc': '2.0', 'result': {'availableBalance': 50, 'lockedAmount': 0}}

    recipients = [{'address': 'abLoc....', 'amount': 50}]
    wallet.send_transaction(transfers=recipients)
    {'id': 0, 'jsonrpc': '2.0', 'result': {'transactionHash': 'ae57e...'}}

Installation
------------

You can install the latest version from PyPI:

.. code-block:: bash

    $ pip3 install bloc

Documentation
-------------

The documentation is available at http://turtlecoin-python.readthedocs.io/

Developer setup
---------------

Clone the repo and install the dependencies with ...pipenv:

.. code-block:: bash

    $ git clone ...
    $ cd bloc-python
    $ pipenv install --dev

To generate the HTML documentation you need to have the bloc module in
your PYTHONPATH. This is used to automatically generate the api docs.
Afterwards you can run the makefile target:

.. code-block:: bash

    $ pipenv run python setup.py develop
    $ pipenv run make html

The documentation on readthedocs is automatically updated on
each push to the master branch (via webhook).

To release a new version on PyPI, increment the version number
in `bloc/__version__.py` and run:

.. code-block:: bash

    $ pipenv run python setup.py upload

This will also create a git tag with the version number.
