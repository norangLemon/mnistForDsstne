import struct
import sys

if len(sys.argv) != 2:
    print("put 'test' or 'train'")
    sys.exit(1)
parsingType = sys.argv[1]
if parsingType != "test" and parsingType != "train":
    print("put 'test' or 'train': %s" % parsingType)
    sys.exit(1)

imageFile = open(parsingType + "-dataset/images", "rb")
labelFile = open(parsingType + "-dataset/labels", "rb")
inputFile = open("result/input-" + parsingType, "w")
outputFile = open("result/output-" + parsingType, "w")


# read image file's header
imageMagicNumber = struct.unpack(">i", imageFile.read(4))[0]
if (imageMagicNumber != 2051):
    print("this is not image file: %d" %imageMagicNumber)
    sys.exit(1)
numImages = struct.unpack(">i", imageFile.read(4))[0]
row = struct.unpack(">i", imageFile.read(4))[0]
col = struct.unpack(">i", imageFile.read(4))[0]
n = row*col

# read label file's header

labelMagicNumber = struct.unpack(">i", labelFile.read(4))[0]
if (labelMagicNumber != 2049):
    print("this is not label file: %d" %labelMagicNumber)
    sys.exit(1)
numItems = struct.unpack(">i", labelFile.read(4))[0]
if (numImages != numItems):
    print("number of Images is not same with number of Index:%d %d" %(numImages, numItems))
    sys.exit(1)

# make dsstne files
print("images: %d\nrow: %d\tcol:%d" % (numImages, row, col))

for i in range (1, numImages+1):
    labelNum = struct.unpack(">B", labelFile.read(1))[0]
    print("\nImage #%d : number %d" % (i, labelNum))
    inputFile.write("case{0}\t".format(i))
    outputFile.write("case{caseIndex}\t{label}\n".format(caseIndex = i, label = labelNum))
    string = ""
    for j in range(1, n):
        pixelNum = struct.unpack(">B", imageFile.read(1))[0]
        inputFile.write("{index},{pixel}:".format(index = j, pixel = pixelNum))
    pixelNum = struct.unpack(">B", imageFile.read(1))[0]
    inputFile.write("{index},{pixel}\n".format(index = n, pixel = pixelNum))
    inputFile.flush()

# close files
imageFile.close()
labelFile.close()
inputFile.close()
outputFile.close()
