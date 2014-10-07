========================================
Existenz 0.0.1 - an existing individual
========================================

**Existenz** in version of Conway's Game of Life.

In it's current form, this is nothing more than a toy commandline application.

Documentation
==============

For the latest documentation, visit http://neoinsanity.github.io/existenz

Getting Existenz
=================

Installation
-------------

Use pip to install existenz.

  > pip install existenz
  
Source
-------

The latest stable release source of **Existenz** can be found on the master 
branch at https://github.com/neoinsanity/existenz/tree/master. 

For the latest development code, use the develop branch at 
https://github.com/neoinsanity/existenz. Please note that the development 
branch may change without notification.

To install **Existenz** from source utilize the *setup.py*:

  > python setup.py install

Project Development
====================

If you are interested in developing **Existenz** code, 
utilize the helper scripts in the *existenz/bin* directory.

Setup the Development Environment
----------------------------------

Prior to running the dev setup scripts, ensure that you have *virtualenv* 
installed. All setup commands are assumed to be run from the project root, 
which is the directory containing the *setup.py* file.

Prep the development environment with the command:

  > bin/dev_setup.sh

This command will setup the virtualenv for the project in the 
directory */venv*. It will also install the **Existenz** in a develop mode, 
with the creation of a development egg file.

Enable the Development Environment
-----------------------------------

To make it easy to ensure a correctly configured development session, 
utilize the command:

  > . bin/enable_dev.sh
  
or

  > source bin/enable_dev.sh
  
Note that the script must be sourced, as it will enable a virtualenv session 
and add the *bin* directory scripts to environment *PATH*.

Running Tests
--------------

To run the unit tests:

  > run_tests.sh

Building Documentation
-----------------------

To run the documentation generation:

  > doc_build.sh
