from typing import Dict, List

import Orange as DM
from Orange.data import DiscreteVariable

from rule1r.oneR_objects import *
from rule1r.print_utils import *


class implementation1R:
    bestAttribute: OneRAttribute = None
    attributesDictionary: Dict[str, OneRAttribute] = None

    def __init__(self, dataset: DM.data.Table):
        self.dataset = dataset
        self.the_class = dataset.domain.class_var

    @staticmethod
    def initialize_attributes_dict(attributes_list: tuple):
        attributesDictionary: Dict[str, OneRAttribute] = dict()

        for atr in attributes_list:
            attributesDictionary[atr] = OneRAttribute(atr)

        return attributesDictionary

    def getBestAtrValue(self, attr: str, attr_value: str, the_class: DiscreteVariable):
        bestOneRObject: OneRObject = None

        for classValue in the_class.values:
            currOneRObject = OneRObject(attr, attr_value, classValue, 0, 0)
            for datasetEntry in self.dataset:

                if datasetEntry[attr] == attr_value:
                    currOneRObject.incrementTotal()
                    if datasetEntry.get_class() != classValue:
                        currOneRObject.incrementError()
            # Updating best object value
            if bestOneRObject is None or bestOneRObject.getErrorRate() > currOneRObject.getErrorRate():
                bestOneRObject = currOneRObject

        return bestOneRObject

    def analyzeWith1R(self):

        self.attributesDictionary = self.initialize_attributes_dict(self.dataset.domain.attributes)

        # Find attributes for each attribute and attribute value

        for atr in self.dataset.domain.attributes:
            for atrValue in atr.values:
                currPair = self.getBestAtrValue(atr, atrValue, self.the_class)
                hypothesisList: List[OneRObject] = self.attributesDictionary.get(atr).hypothesisList
                hypothesisList.append(currPair)

        bestAccuracy: int = None
        for attributeValue in self.attributesDictionary.values():
            currAccuracy = attributeValue.getAccuracy()
            if bestAccuracy is None or bestAccuracy > currAccuracy:
                bestAccuracy = currAccuracy
                self.bestAttribute = attributeValue

    def print1rAnalysis(self):
        if self.bestAttribute is None or self.attributesDictionary is None:
            print("Please analyze the dataset first with the method analyzeWith1R()")
            return

        printHypothesis(self.attributesDictionary)
        printAllAccuracies(self.attributesDictionary)
        printBestAttribute(self.bestAttribute)
