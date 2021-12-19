
# s - string in which the search will take place
# p - pattern

# last - a dictionary of the last positions of
# all alphabetic characters in the pattern p

def bm(text, pattern):
    m = len(pattern)
    t_index = m-1
    p_index = m-1

    while t_index < len(text):
        while text[t_index] == pattern[p_index]:
            t_index -= 1
            p_index -= 1

        if p_index == -1:
            return t_index

        else:
            t_index += m - min(p_index, 1+last(text[t_index]))

    return -1


def last(char):
    for i in Last.keys():
        if i == char:
            return Last[char]

    return -1


p = "Kajak"

s = "Lubie plywac uzywajac Kajaku"
Last = {p_char: p_index for p_index, p_char in enumerate(p)}

print(bm(s, p))
