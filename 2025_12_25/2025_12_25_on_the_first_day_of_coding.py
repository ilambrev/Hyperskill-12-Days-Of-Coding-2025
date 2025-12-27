file_path = "hyperskill-dataset-118993287.txt"

file = open(file_path, "r")
rows = [row.split() for row in file.read().split("\n")]
file.close()

time_frame_begin = 15 * 60
time_frame_end = 15 * 60 + 30

errors = {}

for row in rows:
    hours, minutes = row[0].split(":")
    time_in_minutes = int(hours) * 60 + int(minutes)

    if time_frame_begin <= time_in_minutes <= time_frame_end:
        if row[1] not in errors:
            errors[row[1]] = 0
    
        errors[row[1]] += 1

print(sorted(errors.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)[0][0])