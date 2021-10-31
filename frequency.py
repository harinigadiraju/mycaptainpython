letters = {}
l1 = {}


def most_frequent():
    s = input("Enter a string")
    s.lower()
    for i in s:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    l1 = sorted(letters.items(), key=lambda x: x[1], reverse=True)

most_frequent()
