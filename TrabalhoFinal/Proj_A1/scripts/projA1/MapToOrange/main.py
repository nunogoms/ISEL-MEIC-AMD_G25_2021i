# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

TAB: str = "\t"


def _replaceSeparator(line: str, separator: str):
    return line.replace(separator, TAB)


def removeNewLines(file_contents: List[str]) -> List[str]:
    NEW_LINE = "\n"
    newFileContents: List[str] = []
    for line in file_contents:
        newFileContents.append(line.replace(NEW_LINE, ""))

    return newFileContents


def loadFile(filename: str) -> List[str]:
    try:
        with open(filename, 'r') as filehandle:
            filecontents = filehandle.readlines()
    except:
        print('--->>> error - can not open the file: %s' % filename)
        exit()

    return filecontents


def writeFile(filename: str, file_content: List[str]):
    try:
        with open(filename, 'w') as filehandle:
            filehandle.writelines("%s\n" % line for line in file_content)
    except:
        print('--->>> error - can not write to the file: %s' % filename)
        exit()


def updateColumnNamesLine(first_line: str, separator: str) -> str:
    return _replaceSeparator(first_line, separator)


def addColumnDomains(discrete_columns: List[int], continuous_columns: List[int] = []) -> str:
    totalSize: int = discrete_columns.__len__() + continuous_columns.__len__()
    resultStr: str = ""
    for index in range(0, totalSize):
        if discrete_columns.__contains__(index):
            resultStr += "discrete".__add__(TAB)

        elif continuous_columns.__contains__(index):
            resultStr += "continuous".__add__(TAB)

    return resultStr


def setColumnClass(class_index: int, collumns_size: int) -> str:
    resultStr: str = ""
    for i in range(0, collumns_size):
        if i == class_index: resultStr += "class"
        resultStr += TAB
    return resultStr


def editTuples(tuples: List[str], separator: str) -> List[str]:
    resultStr: List[str] = []
    for line in tuples:
        resultStr.append(_replaceSeparator(line, separator))

    return resultStr


def formatFile(file_contents: List[str], separator: str) -> List[str]:
    if file_contents.__len__() < 2:
        print('--->>> error - this file does not have enough information to be processed')
        exit()

    # normalizing file
    file_contents = removeNewLines(file_contents)

    newFile: List[str] = []
    # first line - collumn names
    newFile.append(updateColumnNamesLine(file_contents[0], separator))
    # second line - data type (continuous/discrete)
    listOfDiscrete = list(range(0, newFile[0].count(TAB)))
    newFile.append(addColumnDomains(listOfDiscrete))
    # add class indication
    newFile.append(setColumnClass(0, listOfDiscrete.__len__()))
    # add tuples normalization
    for tuple in editTuples(file_contents[1:], separator):
        newFile.append(tuple)

    return newFile


def main():
    filename = "../resources/dataset_long_name_ORIGINAL.csv"
    fileContents = loadFile(filename)
    newFileContent = formatFile(fileContents, ",")

    newFileName = "../resources/newDatasetFile.tab"
    writeFile(newFileName, newFileContent)


if __name__ == '__main__':
    main()
