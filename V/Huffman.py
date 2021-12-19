code = {'A': "",
        'B': "",
        'C': "",
        'D': "",
        'E': "",
        'F': ""}

alphabet_list = sorted([(30, "A"), (10, "B"), (20, "C"),
                        (10, "D"), (20, "E"), (10, "F")], reverse=True)


while len(alphabet_list) > 1:
    temp1 = alphabet_list.pop()
    temp2 = alphabet_list.pop()

    for i in temp1[1]:
        code[i] = '1' + code[i]
    for j in temp2[1]:
        code[j] = '0' + code[j]

    alphabet_list.append((temp1[0]+temp2[0], temp1[1]+temp2[1]))
    alphabet_list = sorted(alphabet_list, reverse=True)
