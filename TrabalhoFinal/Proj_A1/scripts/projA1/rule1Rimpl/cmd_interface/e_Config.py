# -*- coding: cp1252 -*-
# ===============================
# author: Paulo Trigo Silva (PTS)
# version: v06
# ===============================


# ______________________________________________________________________________
# The modules to import
import os
import sys
from getopt import getopt, error


# The "getopt" module helps scripts to parse the command line arguments in sys.argv.
# It supports the same conventions as the Unix getopt() function
# (including the special meanings of arguments of the form ‘-‘ and ‘--‘).


# ______________________________________________________________________________
# A class that parses the command line argunmets
# In this example the system has 3 parameters (a, b, c)
# each parameter has a default value that can be redefined as a command line option
class e_Config():
    def __init__(self):
        # definition of default (option, value) pairs
        # i.e., the defualt values for the system parameters: a, b, c
        self.__optionValue = { \
            ("-f", "--file"): "../resources/newDatasetFile"}
            #("-a", "--paramA"): "aaa", \
            #("-b", "--paramB"): 555, \
            #("-c", "--paramC"): "RsR"}

    def obterPairsList(self):
        resultado = list()
        for parOpcao in self.__optionValue.keys():
            resultado.append(parOpcao)
        return list(resultado)

    def config(self, argv):
        smallArgsList = ""
        bigArgsList = list()
        for entry in self.obterPairsList():
            smallArgsList += entry[0].replace('-', '').__add__(":")
            bigArgsList.append(entry[1].replace('--', '').__add__("="))

        # mapped += reduce(lambda key0,key1: key0, optionsValue.keys())
        try:
            try:
                (argv_optionValue, args) = \
                    getopt(argv[1:], \
                           smallArgsList, \
                           [*bigArgsList])
            except error:
                raise Usage(self.usage())
        except Usage as incorrect:
            sys.stderr.write(incorrect.msg)
            sys.exit(2)

        list_optionName = self.__optionValue.keys()
        for (option, value) in argv_optionValue:
            for optionName in list_optionName:
                if option in optionName: self.__optionValue[optionName] = value

    def obterOpcaoValor(self):
        resultado = {}
        for parOpcao in self.__optionValue.keys():
            resultado[parOpcao[0]] = self.__optionValue[parOpcao]
        return list(resultado.items())

    def usage(self):
        smallArgsList = ""
        bigArgsList = ""
        for entry in self.obterPairsList():
            smallArgsList += " %s %s%s" % (entry[0], "value", entry[0].replace('-', '').upper())
            bigArgsList += " %s %s%s" % (entry[1], "value", entry[0].replace('-', '').upper())

        thisFile = os.path.basename(sys.argv[0])
        aStr = ""
        aStr += "\n"
        aStr += "\n" + "Usage:"
        aStr += "\n" + "> " + thisFile + smallArgsList
        aStr += "\n" + "or"
        aStr += "\n" + "> " + thisFile + bigArgsList
        aStr += "\n"
        return aStr


# ______________________________________________________________________________
# Utility Class
# (explores exceptions and decorators such as "getter" and "setter")
class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

    @property
    def msg(self): return self.__msg

    @msg.setter
    def msg(self, value):
        assert isinstance(value, str), "PTS | msg: string expected"
        self.__msg = value

    @msg.deleter
    def msg(self): self.__msg = ""
