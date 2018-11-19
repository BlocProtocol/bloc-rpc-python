.. _blocd:

BLOCd
===========

This document shows how to use the `BLOCd` JSON-RPC API.

Running BLOCd
-------------------

Before you start using the Python integration, make sure that you are
running `BLOCd` with the `enable_blockexplorer` argument set:

.. code-block:: bash

    ./BLOCd --enable_blockexplorer

After starting it make sure the blockchain is synchronized.
This might take a while. The console log will show a message when it's done:

.. code-block:: console

    Successfully synchronized with the BLOC Network

The python integration can now be used.

Usage
-----

For all available methods see the full :ref:`API documentation <blocd_api>`.

To print the current block-height:

.. code-block:: python

    from bloc import BLOCd

    bloc = BLOCd()
    bloc.getblockcount()['count']
    286373
