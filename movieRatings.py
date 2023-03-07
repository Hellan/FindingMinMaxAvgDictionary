'''
Деси много обича да гледа филми, но често й е трудно да си избере подходящ за гледане. Набелязва си
определен брой филми и иска да си избере кой филм да гледа спрямо рейтинга на филмите.
Напишете програма, която показва кой филм е с най-висок рейтинг, кой е с най-нисък и колко е средният
рейтинг от всички филми, които си е набелязала да гледа.
Вход
От конзолата първо се чете един ред:
• Брой филми, които си е набелязала Деси – цяло число в интервала [1…20]
За всеки филм се прочитат два отделни реда:
• Име на филма – текст
• Рейтинг на филма - реално число в интервала [1.00…10.00]
Изход
Отпечатват се три реда в следния формат:
• "{име на филма с най-висок рейтинг} is with highest rating: {рейтинг на филма}"
• "{име на филма с най-нисък рейтинг} is with lowest rating: {рейтинг на филма}"
• "Average rating: {средният рейтинг на всички филми}"
Максималният, минималният и средният рейтинг да се форматира до първата цифра след десетичния знак.
'''
moviesCount = int(input())
moviesDict = {}
for i in range(0,moviesCount):
    name = input()
    rating = float(input())
    moviesDict[name] = rating
minRatingName = min(moviesDict, key=moviesDict.get)
maxRatingName = max(moviesDict, key=moviesDict.get)
minRatingScore = min(moviesDict.values())
maxRatingScore = max(moviesDict.values())
print(f'{maxRatingName} is with highest rating: {maxRatingScore:.1f}')
print(f'{minRatingName} is with lowest rating: {minRatingScore:.1f}')
res = 0
for val in moviesDict.values():
    res += val
average = res / len(moviesDict)
print(f'Average rating: {average:.1f}')
