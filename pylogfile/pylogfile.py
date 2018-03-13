# -*- coding: utf-8 -*-

import datetime as dt
import os

"""Main module."""

class ArquivoDeLog:
    def __init__(self, nome):

        self.__nome = nome
        self.arqlog = nome + '.log'
        self.__log = '\n\n|=====================< ' + now() + ' >=====================|\n' \
            'Log da Aplicacao: ' + nome + '\n'

        self.registra_log('Processo iniciado.')

    def registra_log(self, msg):
        self.__log += now("hora") + ': ' + msg + '\n'

    def mostra_log(self):
        return self.__log

    def grava_arq_log(self):
        with open(self.arqlog, 'a') as alog:
            alog.write(self.__log)
        self.rotaciona_arq_log()

    def rotaciona_arq_log(self):
        if os.stat(self.arqlog).st_size > 5000000:
            try:
                nome_rotat = self.__nome + now('a') + '.log'
                os.rename(self.arqlog, nome_rotat)
            except IOError as e:
                msg = 'Houve um problema ao tentar efetuar a rotatividade do arquivo de log: ' + str(e)
                print(msg)
                self.registra_log(msg)


def now(opc=''):
    data = str(dt.datetime.now())
    escolhas = {
        "ano": data[0:4],
        "mes": data[5:7],
        "dia": data[8:10],
        "hora": data[11:16],
        "nomearq": data[0:13].replace(' ', '').replace('-', '') + '.7z',
        "": data[0:10],
    }
    return escolhas.get(opc, "")
