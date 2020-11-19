fileName = "./dataset_ORANGE.tab"


class Entry:
    def __init__(self, vc1, vc2, vc3):
        self.vc1 = vc1
        self.vc2 = vc2
        self.vc3 = vc3


if len(sys.argv) > 1: fileName = sys.argv[1]

try:
    dataset = DM.data.Table(fileName)
except:
    my_print("--->>> error - can not open the file: %s" % fileName)
    exit()

print("hey")

input("Press Enter to continue...")
input("Press Enter to continue...")
