from string import ascii_lowercase, ascii_uppercase, digits

def is_password_contains_symbols(password, symbols):
    for symbol in symbols:
        if symbol in password:
            return True

    return False

def check_password_categories(categories, score, password):
    for category in categories:
        if not is_password_contains_symbols(password, category):
            score *= 0.75

    return score

def find_most_repeated_symbol(password):
    symbols = {}

    for symbol in password:
        if symbol not in symbols:
            symbols[symbol] = 0

    symbols[symbol] += 1

    return sorted(symbols.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)[0]

file_path = "hyperskill-dataset-119010469.txt"

file = open(file_path, "r")
passwords = file.read().split("\n")
file.close()

symbols = "!@#$%^&*"
best_score = 0
best_password = ""

for password in passwords:
    score = len(password)

    score = check_password_categories(
        [ascii_lowercase, ascii_uppercase, digits, symbols], score, password)
    
    most_repeated_symbol = find_most_repeated_symbol(password)
    
    if  most_repeated_symbol[1] / len(password) > 0.3:
        score -= most_repeated_symbol[1]
    
    if score > best_score:
        best_score = score
        best_password = password

print(best_password)