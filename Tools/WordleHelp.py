import string

word_length = 5
fixed_index = []
fixed_char = []
greatest_frequency = 0
most_likely_word = None

inverse_frequency_score = {
    'e': 26, 't': 25, 'a': 24, 'o': 23, 'i': 22,
    'n': 21, 's': 20, 'h': 19, 'r': 18, 'd': 17,
    'l': 16, 'c': 15, 'u': 14, 'm': 13, 'w': 12,
    'f': 11, 'g': 10, 'y': 9,  'p': 8,  'b': 7,
    'v': 6,  'k': 5,  'j': 4,  'x': 3,  'q': 2,  'z': 1
}



def load_words(filename="words_alpha.txt"):
    with open(filename, "r") as f:
        return set(word.strip().lower() for word in f)

english_words = load_words()


def check(input_value, included_letter):
    count = 0
    global greatest_frequency, most_likely_word
    temp = 0
    seen = []
    for i in input_value:
        temp += inverse_frequency_score.get(i)
        if i in included_letter and i not in seen:
            count += 1
        seen.append(i)
    if input_value.lower() in english_words and count == len(included_letter):
        if temp > greatest_frequency:
            greatest_frequency = temp
            most_likely_word = input_value.lower()
        return True
    else:
        return False

def brute_force(current, position, letters, included_letter):
    if position == word_length:
        if check(current, included_letter):
            print(current)
        return

    if position in fixed_index:
        idx = fixed_index.index(position)
        brute_force(current + fixed_char[idx], position + 1, letters, included_letter)
    else:
        for letter in letters:
            brute_force(current + letter, position + 1, letters, included_letter)

def main():
    global greatest_frequency, most_likely_word
    letters = string.ascii_lowercase

    while True:
        greatest_frequency = 0
        most_likely_word = None
        fixed_index.clear()
        fixed_char.clear()

        input_guess = input("Word guess (use _ for unknowns): ").strip().lower()
        excluded_letter = input("enter excluded letters:")
        included_letter = input("enter included letters:")

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
        brute_force("", 0, letters, included_letter)
        print("=========================================================================")
        print(f"Most Try this next\t{most_likely_word}")
        print("=========================================================================")


if __name__ == "__main__":
    main()
