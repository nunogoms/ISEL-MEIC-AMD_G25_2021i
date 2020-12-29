from typing import Dict

from rule1r.oneR_objects import OneRAttribute


def printHypothesis(attributes_dictionary: Dict[str, OneRAttribute]):
    print("\n - HYPOTHESIS ")
    print("( attr, attr-value, class value ) : (error, total)")

    for attributeOneR in attributes_dictionary.values():
        for hypothesis in attributeOneR.hypothesisList:
            print(hypothesis.toString())


def printAllAccuracies(attributes_dictionary: Dict[str, OneRAttribute]):
    print("\nATTRIBUTE ACCURACY")
    print(" attr : ( error, total ) # error/ total")
    for attributeOneR in attributes_dictionary.values():
        print(attributeOneR.accuracyToString())


def printBestAttribute(attribute: OneRAttribute):
    print("\nONE R ")
    print("( attr, attr-value, class value ) : (error, total)")
    for hypothesis in attribute.hypothesisList:
        print(hypothesis.toString())