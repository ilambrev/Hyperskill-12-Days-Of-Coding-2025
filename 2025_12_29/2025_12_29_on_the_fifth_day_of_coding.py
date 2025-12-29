file_path = "hyperskill-dataset-119052159.txt"

file = open(file_path, "r")
coordinates = [[float(c) for c in row.split(",")] for row in file.read().split("\n")]
file.close()

sum1 = coordinates[-1][0] * coordinates[0][1]
sum2 = coordinates[-1][1] * coordinates[0][0]

sum1 += sum([(coordinates[i][0] * coordinates[i + 1][1]) for i in range(len(coordinates) - 1)])
sum2 += sum([(coordinates[i][1] * coordinates[i + 1][0]) for i in range(len(coordinates) - 1)])

area = abs(sum1 - sum2) / 2

print(round(area, 2))