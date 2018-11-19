bloc-python
=================

.. image:: https://img.shields.io/pypi/v/bloc.svg
	:target: https://pypi.python.org/pypi/bloc

.. image:: https://img.shields.io/pypi/pyversions/bloc.svg
	:target: https://pypi.python.org/pypi/bloc

.. image:: https://img.shields.io/pypi/l/bloc.svg
	:target: https://pypi.python.org/pypi/bloc

bloc-python is a Python wrapper for the BLOC JSON-RPC API.
It integrates with :ref:`walletd` and :ref:`blocd`.

Source Code
-----------

You can find the source code at GitHub: https://github.com/arthurk/bloc-python

Requirements
------------

- Python 3.6
- `BLOC 0.5.0 <https://github.com/bloc/bloc/releases/tag/v0.5.0>`_

Installation
------------

You can install the latest version with pip:

.. code-block:: bash

    $ pip install bloc

Contents
--------

.. toctree::
   :maxdepth: 2

   walletd
   BLOCd

The API Documentation / Guide
-----------------------------

If you are looking for information on a specific function, class, or method,
this part of the documentation is for you.

.. toctree::
   :maxdepth: 2

   api/wallet
   api/daemon

Development
-----------

If you plan to work on the bloc-python itself, it is useful to have
DEBUG logging enabled. You can do this with the following code snippet:

.. code-block:: python

    import logging

    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

Enabling this will let you see more detailed data for the request that is
being sent to the JSON-RPC interface::

    2018-04-05 16:20:09,193 DEBUG    {
        "jsonrpc": "2.0",
        "method": "getlastblockheader",
        "params": {},
        "password": ""
    }
    2018-04-05 16:20:09,204 DEBUG    Starting new HTTP connection (1): 127.0.0.1
    2018-04-05 16:20:09,206 DEBUG    http://127.0.0.1:2086 "POST /json_rpc HTTP/1.1" 200 406
