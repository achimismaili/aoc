# script to solve daily challenges

import re # regular expressions
# import math

### Initialization ###
# defining debug vs. prod data and aoc day
test = False
day = "07"

dataFileName = "data"
if test:
  dataFileName = "sample"

dataFilePath = 'exercises\\day' + day + '\\py\\' + dataFileName + '.txt'


### Program ###

# reading data
fileToOpen = open(dataFilePath, 'r')

text = fileToOpen.read()

# allBags = re.findall(r'^(\w+ \w+) bags contain', text, flags=re.MULTILINE)

def getContainingBags (bagName, body, positives):

  parentBags = re.findall(r'(\w+ \w+) bags contain( \d+ \w+ \w+ bags?,?)* (\d+) ' + bagName + ' bags?', body)

  # print (bags)

  for b in parentBags:
    
    bag = b[0]

    if bag not in positives:
      # print (bag)
      # print (bag.groups(), bag.groups().count)
    
      positives.append(bag)
      positives = getContainingBags (bag, body, positives)
  return positives

def getBagsInBag (bagName, body):
  bagsInBags = 0
  matches = re.findall(rf"^{bagName} bags.*" , body, flags=re.MULTILINE)

  # print (bags)

  for m in matches:
    containedBags = re.findall(r'(contain|,) (\d+) (\w+ \w+) bags?', m)

    for match in containedBags:
      
      containedNumber = int(match[1])
      containedBagName = match[2]
      # print(containedNumber, containedBagName)

      bagsToAdd = containedNumber  
      bagsToAdd += containedNumber * getBagsInBag (containedBagName, body)
      bagsInBags += bagsToAdd

  return bagsInBags

canContain = getContainingBags ("shiny gold", text ,[])
# print (canContain, len(canContain))
print ("Challenge1: {} bag colors can eventually contain at least one shiny gold bag.".format(len(canContain)))

bags = getBagsInBag ("shiny gold", text)
print ("Challenge2: {} individual bags are required inside the single shiny gold bag.".format(bags))


