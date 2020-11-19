# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import Orange as DM

from datasetInstance import DatasetInstance
from u01_util import my_print, print_class, print_attributes


def getInstancesList(dataset: DM.data.Table):
    instancesList = []

    for i in range(0, dataset.__len__()):
        instancesList.append(DatasetInstance(dataset[i]))

    return instancesList


def main():
    fileName = "../dataset_ORANGE.tab"

    if len(sys.argv) > 1: fileName = sys.argv[1]

    try:
        dataset = DM.data.Table(fileName)
    except:
        my_print("--->>> error - can not open the file: %s" % fileName)
        exit()

    print_attributes(dataset)
    print_class(dataset)

    instancesObjList = getInstancesList(dataset)

    input("\nPress Enter to continue...")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
