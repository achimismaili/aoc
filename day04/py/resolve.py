# script to solve daily challenges

# regular expressions
import re

### Configuration / Parameters ###

test = False
day = "04"

dataFileName = "data"
if test:
  dataFileName = "sample"
dataFilePath = 'exercises\\day' + day + '\\py\\' + dataFileName + '.txt'

class Passport(object):
  # def __init__(self, stringLine):
  #   self.addValues(stringLine)
  def addValues(self, stringLine):    
    fieldDict = []
    fieldArray = stringLine.split()
    for fldPair in fieldArray:
      if ':' in fldPair: 
        # source https://www.geeksforgeeks.org/python-convert-key-value-string-to-dictionary/
        fieldDict.append(map(str.strip, fldPair.split(':', 1))) 
    fieldDict = dict(fieldDict)
    # todo: check if dict is empty
    for key in fieldDict:
      # print(key, '->', fieldDict[key])
      if key == "byr":
        
        self.byr = int(fieldDict[key])
      else:
        if key == "iyr":
          self.iyr = int(fieldDict[key])
        else:
          if key == "eyr":
            self.eyr = int(fieldDict[key])
          else:
            if key == "hgt":
              self.hgt = fieldDict[key]
            else:
                    if key == "hcl":
                      self.hcl = fieldDict[key]
                    else:
                      if key == "ecl":
                        self.ecl = fieldDict[key]
                      else:
                        if key == "pid":
                          self.pid = fieldDict[key] # int(fieldDict[key]) --> pid is once 164cm ...
                        else:
                          if key == "cid":
                            self.cid = int(fieldDict[key])
                          else:
                            # todo: throw error
                            pass
  def isOk1(self):
    if self.byr > 0 and self.iyr > 0 and self.eyr > 0 and self.hgt and \
       self.hcl and self.ecl and self.pid:
         return True
    else:
      return False
  def isOk2(self):
    if self.byr >= 1920 and self.byr <= 2002 and \
       self.iyr >= 2010 and self.iyr <= 2020 and \
       self.eyr >= 2020 and self.eyr <= 2030 and \
       self.heightOk() and \
       self.hairColorOk() and \
       self.ecl in self.validEyeColors and \
       self.passportOk():
      return True
    else:
      return False
  def hairColorOk(self):
    p = re.compile('^#[0-9a-f]{6}$')
    if p.match(self.hcl) :
      return True
    else:
      return False
  def heightOk(self):
    p = re.compile('^[0-9]+(in|cm)$') # https://regex101.com/
    if p.match(self.hgt) :
      heightDigits = int(self.hgt[:-2])
      if self.hgt.endswith('in') and heightDigits >= 59 and heightDigits <= 76 :
        return True
      else:
        if self.hgt.endswith('cm') and heightDigits >= 150 and heightDigits <= 193:
          return True
        else:  
          return False
    else:
      return False
  def passportOk(self):
    p = re.compile('^[0-9]{9}$')
    if p.match(self.pid) :
      return True
    else:
      return False
  validEyeColors = {"amb" , "blu" , "brn" , "gry" , "grn" , "hzl" , "oth"}
  byr = 0 # (Birth Year)
  iyr = 0 # (Issue Year)
  eyr = 0 # (Expiration Year)
  hgt = "" # (Height)
  hcl = "" # (Hair Color)
  ecl = "" # (Eye Color)
  pid = "" # (Passport ID)
  cid = 0 # (Country ID)


### Functions ###

def printResult(result, challengeId):
  print()
  print("{} passports are ok in challenge {}.".format(result, challengeId))

def solver(passports):
  passPortsOk1 = 0
  passPortsOk2 = 0
  for p in passports:
    if p.isOk1():
      passPortsOk1 += 1
    if p.isOk2():
      passPortsOk2 += 1
  printResult(passPortsOk1, 1)
  printResult(passPortsOk2, 2)

### Program ###

# reading data
fileToOpen = open(dataFilePath, 'r')

lines = fileToOpen.readlines()

passports = []

passport = Passport()

lastLineWasSpace = False

for line in lines:

  if line.isspace():
    passports.append(passport)
    passport = Passport()
    lastLineWasSpace = True
  else:
    lastLineWasSpace = False
    passport.addValues(line)

if not lastLineWasSpace:
  passports.append(passport)

solver(passports)