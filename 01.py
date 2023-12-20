sentence = input("Введіть речення з двох слів: ")

word1, word2 = sentence.split()

formatted1 = f"{word2.upper()} {word1.capitalize()}"
formatted2 = "{} {}".format(word2.title(), word1.upper())
formatted3 = "{1} {0}".format(word1.capitalize(), word2.title())

print(formatted1, formatted2, formatted3, sep = "<<<>>>")



















# word1, word2 = a.split()




