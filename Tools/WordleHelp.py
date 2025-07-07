import string

word_length = 5

fixed_index = []
fixed_char = []


def load_words(filename="words_alpha.txt"):
    with open(filename, "r") as f:
        return set(word.strip().lower() for word in f)

english_words = load_words()


def check(input_value):
    return input_value.lower() in english_words

def brute_force(current, position, letters):
    if position == word_length:
        if check(current):
            print(current)
        return

    if position in fixed_index:
        idx = fixed_index.index(position)
        brute_force(current + fixed_char[idx], position + 1, letters)
    else:
        for letter in letters:
            brute_force(current + letter, position + 1, letters)

def main():
    letters = string.ascii_lowercase

    while True:
        fixed_index.clear()
        fixed_char.clear()

        input_guess = input("Word guess (use _ for unknowns): ").strip().lower()
        excluded_letter = input("enter excluded letters:")

        for i in excluded_letter:
            letters = letters.replace(i,"")

        if input_guess == "quit":
            break
        if len(input_guess) != word_length:
            print(f"Word must be exactly {word_length} characters.")
            continue

        for i, char in enumerate(input_guess):
            if char != '_':
                fixed_index.append(i)
                fixed_char.append(char)

        print("Searching for valid words...")
        brute_force("", 0, letters)

if __name__ == "__main__":
    main()
