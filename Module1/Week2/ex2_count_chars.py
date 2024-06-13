def count_chars(str):
    result = {}
    for ch in str:
        if ch not in result:
            result[ch] = 1
        else:
            result[ch] = result[ch] + 1

    print(result)


string = "Happiness"
count_chars(string)


string = "smiles"
count_chars(string)
