# script to solve daily challenges

### Configuration / Parameters ###

day = "02"
dataFilePath = 'exercises\\day' + day + '\\py\\data.txt'

### Functions ###

def calculate1(line):
  # print(line)
  minmaxp, letter, password = line.split()
  occurances = password.count(letter[:1])
  minp, maxp = minmaxp.split('-')
  # print(occurances, int(minp), int(maxp))
  if int(minp) <= occurances and int(maxp) >= occurances:
    return True
  return False

def calculate2(line):
  # print(line)
  minmaxp, letter, password = line.split()
  minp, maxp = minmaxp.split('-')
  first = password[int(minp)-1] == letter[:1]
  second = password[int(maxp)-1] == letter[:1]
  # print(first)
  # print(second)
  if first != second:
    return True
  return False

# function to call the two challenge calculating furnctions for the day and print result
def solver(data, challengeId):
  validPolicies = 0
  for line in data:
    if challengeId == 1 and calculate1(line):
      validPolicies += 1
    elif challengeId == 2 and calculate2(line):
      validPolicies += 1
  print()
  print("{} valid policies found for challenge {}.".format(validPolicies, challengeId))

### Program ###

# reading data
fileToOpen = open(dataFilePath, 'r')

data = fileToOpen.readlines()

solver(data, 1)
solver(data, 2)