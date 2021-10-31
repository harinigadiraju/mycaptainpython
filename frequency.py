letters = {}
def most_frequent():
    s = input("Enter a string : ")
    s.lower()
    for i in s:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    print(letters)

most_frequent()
