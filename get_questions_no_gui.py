import csv

file = open("EPL_Stadiums.csv", "r")
all_stadiums = list(csv.reader(file, delimiter=","))
file.close()

# remove the first row (header values)
all_stadiums.pop(0)


print(all_stadiums[:21])

print("Length: {}".format(len(all_stadiums)))