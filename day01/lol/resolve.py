# arrange
reports = []
with open(".\day01\lol\data.txt", "r") as file:
    for line in file:
        reports.append(int(line))

reports.sort()

# act
for r in reports:
    print (r)
# assert


# i = 1
# while i <= 6:
#     print(i)
#     i += 1
