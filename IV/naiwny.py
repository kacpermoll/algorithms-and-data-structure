text = input("Podaj tekst: ")
pattern = input("Podaj wzorzec: ")
counter = 0
for t_index, t_character in enumerate(text):
    for p_index, p_character in enumerate(pattern):
        if text[t_index+p_index] == pattern[p_index]:
            counter += 1
        else:
            break

        if counter == len(pattern):
            print(t_index)

    counter = 0
