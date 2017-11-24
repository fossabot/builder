builder
########################################

builder is a command line tool to help sysadmin packaging **binaries**

As I am essentially working on **red hast** _based_ distributions, **builder** will prio target `rpm` packages.

However, other **binary** formats, will follow.

Main features
=============

* RPM building


Installation
============


Python version
--------------

Although Python 2 **SHOULD** be *supported*, it is recommended to install
*builder* against the latest Python 3.x whenever possible.

See travis configuration file for tested python versions


Unstable version
----------------

You can also instead of the latest the latest unreleased development version
directly from the ``master`` branch on GitHub.
It is a work-in-progress of a future stable release so the experience
might be not as smooth.

.. code-block:: bash

    $ pip install git+https://github.com/waghanza/builder.git@master#builder


Usage
=============

Building could be made on any cloud, but

+ Build a RPM for **Amazon Linux** `2017.09`

.. code-block:: bash

  $ builder build-rpm -s ~/workspace/specs/python-six.spec -i ami-8c1be5f6

