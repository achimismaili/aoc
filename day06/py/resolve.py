# script to solve daily challenges

# regular expressions
# import re

# math
import math

### Initialization ###
# defining debug vs. prod data and aoc day
test = False
day = "06"

# defining global variables and assigning default values

# global variables
totalOrYes = 0
totalAndYes = 0

# group variables
emptyGroup = "{0:b}".format(0).zfill(26)
groupId = 1
groupOrYes = emptyGroup
groupAndYes = emptyGroup
newGroupStarts = True # global var to know, when a new group will start, relevant for AND
finalAdd = False # global var, just to know, if last row was not empty

dataFileName = "data"
if test:
  dataFileName = "sample"

dataFilePath = 'exercises\\day' + day + '\\py\\' + dataFileName + '.txt'

### Functions ###
def binaryOr(binStr1, binStr2):
  # converts two bin strings to binary, makes OR compare, and returns binary back as string
  # https://pythonspot.com/binary-numbers-and-logical-operators/
  bin1 = int(binStr1, 2)
  bin2 = int(binStr2, 2)
  binOr = bin1 | bin2

  # convert back to string, see https://mkyong.com/python/python-how-to-convert-int-to-a-binary-string/
  return "{0:b}".format(binOr).zfill(26)

def binaryAnd(binStr1, binStr2):
  # converts two bin strings to binary, makes AND compare, and returns binary back as string
  # https://pythonspot.com/binary-numbers-and-logical-operators/
  bin1 = int(binStr1, 2)
  bin2 = int(binStr2, 2)
  binOr = bin1 & bin2

  # convert back to string, see https://mkyong.com/python/python-how-to-convert-int-to-a-binary-string/
  return "{0:b}".format(binOr).zfill(26)


### Reporting / Logging functions ###
def printGrpReturnOr(result, grpId):
  print("Group #{} 'or' result is {}".format(grpId, result))
  return result

def printGrpReturnAnd(result, grpId):
  print("Group #{} 'and' result is {}".format(grpId, result))
  return result

def printResult(result, challengeId):
    print("{} is the sum of 'yes' answers for challenge {}.".format(result, challengeId))


### Program ###

# reading data
fileToOpen = open(dataFilePath, 'r')
rows = fileToOpen.readlines()

for r in rows:

  row = r.strip() # remove new line

  if not row:
    # empty row - here, the end of a group calculation is reached
    totalOrYes += printGrpReturnOr(groupOrYes.count('1'), groupId)
    groupOrYes = emptyGroup # reset is not needed if always only one new line between
    
    totalAndYes += printGrpReturnAnd(groupAndYes.count('1'), groupId)
    groupAndYes = emptyGroup # reset is not needed if always only one new line between 

    finalAdd = False
    newGroupStarts = True
    groupId += 1

  else:
    # here, group calculation takes place
    ASCIIstart = 97 # https://www.programiz.com/python-programming/examples/ascii-character
    # print("The start value of 'a' is", ord('a') - ASCIIstart) # --> result of a is 97
    # print("The ASCII value of 'z' is", ord('z') - ASCIIstart) 
    
    thisAnswer = 0 # reset/init variable

    # add each letter to right binary value according to ASCII order 0 - 25 binary digits
    for c in row:
      answerIndex = ord(c) - ASCIIstart
      thisAnswer += math.pow(2, answerIndex) # see also https://www.tutorialspoint.com/python/number_pow.htm

    # convert int to a string with twentysix characters/digits (--> 0 or 1)
    thisAnswerAsBinString = format(int(thisAnswer), "b") 

    # Attention! In case of AND, a new group must not start with existing zeros and being compared
    # with first answer, otherwise AND compare would always result in zero only
    # For OR, this would not cause an error, when empty string would be compared with first answer.
    if newGroupStarts:
      # store first response in group variables
      groupOrYes = thisAnswerAsBinString
      groupAndYes = thisAnswerAsBinString
      newGroupStarts = False
    else:
      # compare 'OR' to previous answers and store in OR-group variable
      groupOrYes = binaryOr(groupOrYes,thisAnswerAsBinString )
      # compare 'AND' to previous answers and store in AND-group variable
      groupAndYes = binaryAnd(groupAndYes,thisAnswerAsBinString )

    finalAdd = True

if finalAdd:
    totalOrYes += printGrpReturnOr(groupOrYes.count('1'), groupId)
    totalAndYes += printGrpReturnAnd(groupAndYes.count('1'), groupId)

printResult(totalOrYes, 1)
printResult(totalAndYes, 2)