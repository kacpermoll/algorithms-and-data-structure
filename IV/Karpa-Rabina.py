def kp(text, pattern, alphabet):
    q_mod = 23
    t_hash = 0
    p_hash = 0
    m = len(pattern)

    for i in range(m):
        # making first hashes
        p_hash = (p_hash * len(alphabet) + alphabet[pattern[i]]) % q_mod
        t_hash = (t_hash * len(alphabet) + alphabet[text[i]]) % q_mod

    i = 0
    while i <= len(text) - len(pattern):
        if t_hash == p_hash:
            if text[i:i+len(pattern)] == pattern:
                return i
        t_hash = ((t_hash - (alphabet[text[i]] * pow(len(alphabet), m-1))) * len(
            alphabet) + alphabet[text[i+m]]) % q_mod

        i += 1
    return -1


text = "Ala ma kota"
pattern = "kot"
alphabet = {}
for y, x in enumerate(text):
    if x not in alphabet.keys():
        alphabet[x] = y
print(kp(text, pattern, alphabet))
