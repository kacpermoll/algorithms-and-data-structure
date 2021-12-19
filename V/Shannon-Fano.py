

def sf(alphabet_list):
    if len(alphabet_list) > 1:
        left = []
        right = alphabet_list

        left_sum, right_sum = 0, 0

        for i in right:
            right_sum += i[0]

        i = 0
        while i < len(alphabet_list):
            # when the absolute value of the difference of
            # (left side value + first element from right side)
            # and
            # (left side value - first element from right side)
            # is less than the absolute value of the difference of sumed left side value - right side value
            if abs((left_sum+right[0][0]) - (right_sum-right[0][0])) < abs(right_sum - left_sum):
                temp = right.pop(0)
                left.append(temp)
                left_sum += temp[0]
                right_sum -= temp[0]
                i += 1
            else:
                break

        # for each letter/character in left side append "0"
        for i in left:
            code[i[1]] += "0"
        # for each letter/character in right side append "1"
        for j in right:
            code[j[1]] += "1"

        sf(left)
        sf(right)


code = {'A': "",
        'B': "",
        'C': "",
        'D': "",
        'E': "",
        'F': ""}

alphabet_list = sorted([(30, "A"), (10, "B"), (20, "C"),
                        (10, "D"), (20, "E"), (10, "F")], reverse=True)


sf(alphabet_list)
print("Wyznaczony kod: ", code)
tekst = "ABCD"
print("Tekst: ", tekst, "\nZakodowany tekst: ", end="")
for litera in tekst:
    print(code[litera], end="")
