# script to solve daily challenges

# regular expressions
# import re

### Configuration / Parameters ###

test = False
day = "05"

dataFileName = "data"
if test:
  dataFileName = "sample"

dataFilePath = 'exercises\\day' + day + '\\py\\' + dataFileName + '.txt'

### Classes ###

class Seat(object):
  def __init__(self, boardingPass):
    # logic to be added here

    self.row = int(boardingPass[:7].translate(str.maketrans({'F': '0', 'B': '1'})), 2)
    self.column = int(boardingPass[7:].translate(str.maketrans({'L': '0','R': '1'})) , 2)

    # print("{}: row {}, column {}, seat ID {}.".format(boardingPass, self.row, self.column, self.SeatId()))

  def SeatId(self):
    return self.row * 8 + self.column

  row = 0 # (seat row 0 to 127)
  column = 0 # (seat column 0 to 7)

### Functions ###
# see method #3 at https://www.geeksforgeeks.org/python-find-missing-numbers-in-a-sorted-list-range/
def find_missing(lst): 
    return sorted(set(range(lst[0], lst[-1])) - set(lst)) 

def printResult(result, challengeId):
  print()
  if challengeId == 1:
    print("{} is the highest seat for challenge {}.".format(result, challengeId))
  else:
    print("{} are missing seats for challenge {}.".format(result, challengeId))
  

def solver(rows):
  seatIds = []
  
  for r in rows:
    seatIds.append((Seat(r.strip())).SeatId())
  
  printResult(max(seatIds), 1)

  mySeat = find_missing(sorted(seatIds))

  printResult(mySeat, 2)

### Program ###

# reading data
fileToOpen = open(dataFilePath, 'r')

lines = fileToOpen.readlines()

solver(lines)
