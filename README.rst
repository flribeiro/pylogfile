=========
PyLogFile
=========


.. image:: https://img.shields.io/pypi/v/pylogfile.svg
        :target: https://pypi.python.org/pypi/pylogfile

.. image:: https://img.shields.io/travis/flribeiro/pylogfile.svg
        :target: https://travis-ci.org/flribeiro/pylogfile

.. image:: https://readthedocs.org/projects/pylogfile/badge/?version=latest
        :target: https://pylogfile.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Class to create an object for log file manipulation.


* Free software: MIT license
* Documentation: https://pylogfile.readthedocs.io.


Features
--------

* `var = ArquivoDeLog('nameapp')` - create a new ArquivoDeLog object using 'nameapp' as the application logged name.
* var.registra_log('something') - store 'something' in the log text for this session/object preceded by the system time (hour and minute).
* var.mostra_log() - shows the current log.
* var.grava_arq_log() - write log content to the file 'nameapp.log'.
* var.rotaciona_arq_log() - starts a new log file if the previous one surpassed 5 MB.
* function now() - returns current system time.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
