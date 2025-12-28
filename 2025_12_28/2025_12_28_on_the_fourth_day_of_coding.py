file_path = "hyperskill-dataset-119029174.txt"

file = open(file_path, "r")
logs = [row.split(",") for row in file.read().split("\n")]
file.close()

forks_states = {
    "1": "release",
    "2": "release",
    "3": "release",
    "4": "release",
}
elves_forks = {
    "Jingle": ["1", "4"],
    "Sparkle": ["1", "2"],
    "Tinsel": ["2", "3"],
    "Holly": ["3", "4"]
}

contentions = 0

for log in logs:
    elve, action, fork = log

    if fork not in elves_forks[elve] or forks_states[fork] == action:
        contentions += 1
        continue

    forks_states[fork] = action

print(contentions)