from typing import List, Dict


class OneRObject:
    def __init__(self, attr: str, value_attr: str, value_target: str, error: int, total: int):
        self.attr = attr
        self.valueAttr = value_attr
        self.valueTarget = value_target
        self.error = error
        self.total = total

    def getErrorRate(self):
        return self.error / self.total

    def incrementError(self):
        self.error += 1

    def incrementTotal(self):
        self.total += 1

    def toString(self):
        return "('%s', '%s', '%s') : (%s, %s) " % (self.attr, self.valueAttr, self.valueTarget, self.error, self.total)


class OneRAttribute:
    total = 0
    error = 0

    def __init__(self, attr_name: str):
        self.attrName = attr_name
        self.hypothesisList: List[OneRObject] = list()

    def getAccuracy(self):

        if self.total == 0 and self.error == 0:
            totalNumber: int = 0
            totalError: int = 0
            for oneRObject in self.hypothesisList:
                totalNumber += oneRObject.total
                totalError += oneRObject.error

            self.total = totalNumber
            self.error = totalError

        return self.error / self.total

    def accuracyToString(self):
        accuracy = self.getAccuracy()

        return "%s : (%s, %s) # %s" % (self.attrName, self.error, self.total, accuracy)
