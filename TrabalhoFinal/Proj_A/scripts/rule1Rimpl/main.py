# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

import Orange as DM

from cmd_interface.e_Config import e_Config
from rule1r.implementation1R import implementation1R


def load(fileName):
    try:
        dataset = DM.data.Table(fileName)
    except:
        print('--->>> error - can not open the file: %s' % fileName)
        exit()

    return dataset

def main():
    e = e_Config()
    e.config(sys.argv)
    filename = e.obterOpcaoValor().__getitem__(0)[1].__str__()
    print(filename)

    dataset = load(filename)

    print("\n\n\n")

    oneRImpl = implementation1R(dataset)
    oneRImpl.analyzeWith1R()
    oneRImpl.print1rAnalysis()

    print("\n")
    input("Press Enter to exit...")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
