import string


def cezar(text, key):
    text = text.lower()
    alphabet = list(string.ascii_lowercase)
    code = []
    for t_char in text:
        for a_index, a_char in enumerate(alphabet):
            if t_char == " ":
                code.append(" ")
                break
            if t_char == a_char:
                code.append(alphabet[(a_index+key) % len(alphabet)])
                break

    return code


def main():
    print(cezar("Twoja stara", 3))


if __name__ == "__main__":
    main()
