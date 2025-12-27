from math import ceil

file_path = "hyperskill-dataset-118997363.txt"

file = open(file_path, "r")
input_rows = file.read().split("\n")
file.close()

target_sweetness = int(input_rows[0])
sweetness_levels = [int(level) for level in input_rows[1].split(",")]

closest_switness = (sweetness_levels[0] + sweetness_levels[1]) / 2

for i in range(len(sweetness_levels) - 1):
    for j in range(i + 1, len(sweetness_levels)):
        average_sweetness = (sweetness_levels[i] + sweetness_levels[j]) / 2
        difference = abs(target_sweetness - average_sweetness)

        if difference < abs(target_sweetness - closest_switness):
            closest_switness = average_sweetness

print(ceil(closest_switness))