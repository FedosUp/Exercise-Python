import zip_util
from math import radians
zip_codes = zip_util.read_zip_all()
print(zip_codes[0])

#Функция поиска по индексу
def loc(a):
    for i in zip_codes:
        if int(i[0:][0]) == a:
            print(f'ZIP Code {i[0]} is in {i[3]}, {i[4]}, {i[5]} county, coordinates: ({radians(i[1])}, {radians(i[2])})')
            break
        else:
            print("Ошибка! Данный индекс не найден.")
            break
# Функция поиска почтовых индексов по городу и штату
def zipfinder(a, b):
    ziplist =[]
    for i in zip_codes:
        if str(i[0:][3]) == a.title() and str(i[0:][4]) == b.upper():
            #str(i[4]) == b
            ziplist.append(i[0])
    print(f'The following ZIP Code(s) found for {a.capitalize()}, {b.upper()}: ' + ', '.join(ziplist))
        # else:
        #     print("Ошибка! Данный индекс не найден.")

#Выбор команды
com = input("Command ('loc', 'zip', 'dist', 'end'): ")
print(com)
if com.lower() == 'loc':
    loc(int(input('Enter a ZIP Code to lookup: ')))
elif com.lower() == 'zip':
    city = input('Enter a city name to lookup: ')
    print(city)
    state = input('Enter the state name to lookup: ')
    print(state)
    zipfinder(str(city), str(state))