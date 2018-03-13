=====
Usage
=====

To use PyLogFile in a project::

    >>> from pylogfile import ArquivoDeLog
    >>> var = ArquivoDeLog('nameapp')
    >>> var.registra_log('something')
    >>> var.mostra_log()
    >>> var.grava_arq_log() - write log content to the file 'nameapp.log'.
    >>> var.rotaciona_arq_log() - starts a new log file if the previous one surpassed 5 MB.
