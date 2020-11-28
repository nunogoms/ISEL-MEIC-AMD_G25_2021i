import uncompyle6


def work():
    with open("uncompiled_file_1R.py", "wb") as fileobj:
        uncompyle6.uncompyle_file("oneR_classifier.pyc", fileobj)
