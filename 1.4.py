def are_anagrams(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)
user_word1 = input("Введите первое слово: ")
user_word2 = input("Введите второе слово: ")
if are_anagrams(user_word1, user_word2):
    print("Слова являются анаграммами.")
else:
    print("Слова не являются анаграммами.")