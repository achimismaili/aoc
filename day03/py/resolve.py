# script to solve daily challenges

### Configuration / Parameters ###

day = "03"
dataFilePath = 'exercises\\day' + day + '\\py\\data.txt'

### Functions ###

def calculate(data, right, down):
   
  trees = 0
  position = 0
  skipFirstRow = True
  
  lineLength = 0
  
  row = 0

  for line in data:
    row += 1
    if skipFirstRow:
      skipFirstRow = False
      # only needs to be evaluated once
      lineLength = len(line.strip())
      continue

    if not (row + 1) % down == 0:
      continue

    # print(line, position)
    
    position += right
    if position >= lineLength:
      position -= lineLength

    if line[position] == '#':
      trees += 1
  
  return trees

def calculate2 (data):
  slope1 = calculate (data, 1, 1)
  slope2 = calculate (data, 3, 1)
  slope3 = calculate (data, 5, 1)
  slope4 = calculate (data, 7, 1)
  slope5 = calculate (data, 1, 2)

  # print(slope1, slope2, slope3, slope4, slope5)

  return slope1 * slope2 * slope3 * slope4 * slope5

# function to call the two challenge calculating furnctions for the day and print result
def solver(data, challengeId):
  trees = 0
  if challengeId == 1:
    trees = calculate(data, 3, 1)
  elif challengeId == 2:
    trees = calculate2(data)
  print()
  print("{} trees found for challenge {}.".format(trees, challengeId))

### Program ###

# reading data
fileToOpen = open(dataFilePath, 'r')

data = fileToOpen.readlines()

solver(data, 1)
solver(data, 2)