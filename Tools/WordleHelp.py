from PyMultiDictionary import MultiDictionary

dictionary = MultiDictionary()

def check(input_value):
    if not dictionary.meaning("en", input_value):
        return False
    return True


def wordleHelp(input_value):
    return_list = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in input_value:
        if i.equals('_'):
            for j in alphabet:
                pass
    return return_list

def main():
    while True:
        output = wordleHelp(input("word guess:"))
        for i in output:
            print(i)

if __name__ == "__main__":
    main()