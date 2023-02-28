text = input()
text = text.replace(" ", "")
text = list(text)
vowels = "ауоиэыяюеё"
changes = 0

for i in range(len(text - 1)):
    if text[i] in vowels:
        text[i + 1] in vowels
        #добавляем к счетчику изменений 1
        #заменить следующую букву на согласную
    else:
        text[i + 1] not in vowels
        #добавляем к счетчику изменений 1
        #заменить следующую букву на гласную

print(changes)