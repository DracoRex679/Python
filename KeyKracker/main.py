word = input()

keys = ["a", "b", "c", "d",
       "e", "f", "g", "h",
       "i", "j", "k", "l",
       "m", "n", "o", "p",
       "q", "r", "s", "t",
       "u", "v", "w", "x",
       "y", "z"]
for i in range(26):
    original_letters = []
    for char in word.lower():
        original_letters.append(char)
    letters = original_letters
    for letter in range(len(letters)):
        for key in range(len(keys)):
            if letters[letter] == keys[key]:
                if key + i > 25:
                    rotation = key + i - 26
                    data = keys[rotation]
                    letters[letter] = data
                else:
                    data = keys[key+i]
                    letters[letter] = data
                break
    print(letters)



