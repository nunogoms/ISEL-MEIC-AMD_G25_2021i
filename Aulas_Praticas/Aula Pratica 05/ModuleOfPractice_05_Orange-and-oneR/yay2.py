# uncompyle6 version 3.7.4
# Python bytecode 3.6 (3379)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04)
# [GCC 7.5.0]
# Warning: this version of Python has problems handling the Python 3 "byte" type in constants properly.

# Embedded file name: ./oneR_classifier.py
# Compiled at: 2019-10-22 13:51:46
# Size of source mod 2**32: 6769 bytes
import Orange as DM, random

# Some Utility Functions
def my_print( aStr ):
   separator = lambda x: "_" * len( x )
   print( separator( aStr ) )
   print( aStr )


def load(fileName):
    try:
        dataset = DM.data.Table(fileName)
    except:
        my_print('--->>> error - can not open the file: %s' % fileName)
        exit()

    return dataset


class OneR:

    def classify(self, dataset):
        self.attrValueTargetCOUNT = {}
        self.attrSet = [x.name for x in dataset.domain.attributes]
        self.valueAttrSet = {}
        self.valueTargetSet = []
        for line in range(len(dataset)):
            dataTuple = dataset[line]
            for attr in self.attrSet:
                valueAttr = str(dataTuple[attr])
                valueTarget = str(dataTuple[dataset.domain.class_var])
                AVT = (attr, valueAttr, valueTarget)
                self.attrValueTargetCOUNT[AVT] = self.attrValueTargetCOUNT.get(AVT, 0) + 1
                self.valueAttrSet = addToDictValueSet(attr, valueAttr, self.valueAttrSet)
                if valueTarget not in self.valueTargetSet:
                    self.valueTargetSet += [valueTarget]

        self.HYPOTHESES = {}
        for attr in self.attrSet:
            for valueAttr in self.valueAttrSet[attr]:
                AVT_max = None
                freq_max = -1
                freq_total = 0
                for valueTarget in self.valueTargetSet:
                    AVT = (
                        attr, valueAttr, valueTarget)
                    freq = self.attrValueTargetCOUNT.get(AVT)
                    if freq:
                        freq_total += freq
                        r = -1
                        if freq == freq_max:
                            r = random.randint(0, 1)
                        if r == 0 or freq > freq_max:
                            freq_max = freq
                            AVT_max = AVT

                if AVT_max:
                    error = freq_total - freq_max
                    self.HYPOTHESES[AVT_max] = (error, freq_total)

        self.attrACCURACY = {}
        for attr in self.attrSet:
            error_sum = 0
            total_attrValueTarget_sum = 0
            for valueAttr in self.valueAttrSet[attr]:
                for valueTarget in self.valueTargetSet:
                    AVT = (
                        attr, valueAttr, valueTarget)
                    AVT_tuple = self.HYPOTHESES.get(AVT)
                    if AVT_tuple:
                        error, total_attrValueTarget = AVT_tuple
                        error_sum += error
                        total_attrValueTarget_sum += total_attrValueTarget

            self.attrACCURACY[attr] = (
                error_sum, total_attrValueTarget_sum)

        attrMIN = None
        error_min = 1.0
        for attr in self.attrSet:
            error_total = self.attrACCURACY.get(attr)
            if error_total:
                error, total = error_total
                error_cur = float(error) / float(total)
                r = -1
                if error_cur == error_min:
                    r = random.randint(0, 1)
                if r == 0 or error_cur < error_min:
                    error_min = error_cur
                    attrMIN = attr

        self.ONE_R = {}
        for valueAttr in self.valueAttrSet[attrMIN]:
            for valueTarget in self.valueTargetSet:
                AVT = (
                    attrMIN, valueAttr, valueTarget)
                AVT_tuple = self.HYPOTHESES.get(AVT)
                if AVT_tuple:
                    self.ONE_R[AVT] = AVT_tuple

    def toString(self):
        result = ''
        result += self.str_attrValueTargetCOUNT()
        result += self.str_HYPOTHESES()
        result += self.str_ACCURACY()
        result += self.str_ONE_R()
        return result

    def str_attrValueTargetCOUNT(self):
        result = '\n'
        result += '- attrValueTargetCOUNT' + '\n'
        result += '- ( attr, value, target ) : COUNT' + '\n'
        for attr in self.attrSet:
            for valueAttr in self.valueAttrSet[attr]:
                for valueTarget in self.valueTargetSet:
                    AVT = (
                        attr, valueAttr, valueTarget)
                    if self.attrValueTargetCOUNT.get(AVT):
                        result += str(AVT) + ' : ' + str(self.attrValueTargetCOUNT[AVT]) + '\n'

        return result

    def str_HYPOTHESES(self):
        result = '\n'
        result += '- HYPOTHESES\n'
        result += '- ( attr, valueAttr, valueTarget ) : (error, total)' + '\n'
        for attr in self.attrSet:
            for valueAttr in self.valueAttrSet[attr]:
                for valueTarget in self.valueTargetSet:
                    AVT = (
                        attr, valueAttr, valueTarget)
                    if self.HYPOTHESES.get(AVT):
                        result += str(AVT) + ' : ' + str(self.HYPOTHESES[AVT]) + '\n'

        return result

    def str_ACCURACY(self):
        result = '\n'
        result += 'attrACCURACY\n'
        result += '- attr : ( error, total ) # error / total' + '\n'
        for attr in self.attrSet:
            error_total = self.attrACCURACY[attr]
            error, total = error_total
            result += str(attr) + ' : ' + str(error_total) + ' # ' + str(float(error) / float(total)) + '\n'

        return result

    def str_ONE_R(self):
        result = '\n'
        result += 'ONE_R\n'
        result += '- ( attr, valueAttr, valueTarget ) : (error, total)' + '\n'
        for option in self.ONE_R.keys():
            result += str(option) + ' : ' + str(self.ONE_R[option]) + '\n'

        return result


def addToDictValueSet(aKey, aValue, aDict):
    theSet = aDict.get(aKey, [])
    if aValue not in theSet:
        theSet += [aValue]
        aDict[aKey] = theSet
    return aDict


if __name__ == '__main__':
    oneR = OneR()
    dataset = load('./_dataset/lenses')
    oneR.classify(dataset)
    print(oneR.toString())