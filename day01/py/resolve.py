# script to solve day 01 challenges
# Link how to handle array elements https://stackoverflow.com/questions/13732025/get-array-elements-from-index-to-end

### Configuration / Parameters ###

target = 2020
day = "01"
dataFilePath = 'exercises\\day' + day + '\\py\\data.txt'

### Functions ###

# function to find the 2 entries that sum to target and then multiply those 2 numbers together
def calculate2numbers(nums):

  # todo: include check, that array contains at least 2 numbers

  for i in range(0, len(nums)-2):
      pendant = target - nums[i]

      if pendant in nums[i+1:-1]:
        print("Result for 2 numbers: {} * {} = {}".format( nums[i], pendant, nums[i] * pendant))
        break

# function to find the 3 entries that sum to target and then multiply those 3 numbers together
def calculate3numbers(nums):

  # todo: include check, that array contains at least 3 numbers

  for i in range(0, len(nums)-3):
      first = nums[i]
      rest = target - first

      for j in range(i + 1, len(nums)-2):
        second = nums[j]
        third = rest - second

        if third in nums[j+1:-1]:
          print("Result for 3 numbers: {} * {} * {} = {}".format( first, second, third, first * second * third))
          return

### Program ###

# reading data
fileToOpen = open(dataFilePath, 'r')
data = fileToOpen.readlines()
numbers = [int(i) for i in data]

# first challenge
calculate2numbers(numbers)

# second challenge
calculate3numbers(numbers)

