#Задача "Однокоренные":
def single_root_words(root_word, *other_words): #Объявляем фунцию
    root_word_lower = root_word.lower()
    same_words = [] #Создаем пустой список
    for word in other_words: #Перебираем слова
        word_lower = word.lower()
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)
    return same_words #Возвращаем список

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
