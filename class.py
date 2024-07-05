import zip_util
zip_codes = zip_util.read_zip_all()
com = ''
class ZIP:
    # def __init__(self, value):
    #     self.repr_value = []

    def loc(zip):
        for i in zip_codes:
            if int(i[0:][0]) == zip:
                print(f'ZIP Code {i[0]} is in {i[3]}, {i[4]}, {i[5]} county, coordinates: ({i[1]}, {i[2]})')
                break
        else:
            print("Ошибка! Данный индекс не найден.")

    def zipfinder(a, b):
        ziplist = []
        for i in zip_codes:
            if str(i[0:][3]) == a.title() and str(i[0:][4]) == b.upper():
                ziplist.append(i[0])
        if len(ziplist) > 0:
            print(f'The following ZIP Code(s) found for {a.capitalize()}, {b.upper()}: ' + ', '.join(ziplist))
        else:
            print("Ошибка! Данные не найдены.")


    # Функция поиска расстояния между двумя индексами
    def distination(zip1, zip2):
        zip1points = []
        zip2points = []

        for i in zip_codes:
            if int(i[0:][0]) == zip1:
                zip1points.extend([i[1], i[2]])
            elif int(i[0:][0]) == zip2:
                zip2points.extend([i[1], i[2]])
        if len(zip1points) > 0 and len(zip2points) > 0:
            distance = haversine(zip1points, zip2points, unit=Unit.MILES)
            print(f'The distance between {zip1} and {zip2} is {round(distance, 2)}  miles')
        else:
            print("Ошибка! Индекс не найден.")

while com.lower() != 'end':
    com = input("Command ('loc', 'zip', 'dist', 'end'): ")
    print(com)
    if com.lower() == 'loc':
        ZIP.loc(int(input('Enter a ZIP Code to lookup: ')))
    elif com.lower() == 'zip':
        city = input('Enter a city name to lookup: ')
        print(city)
        state = input('Enter the state name to lookup: ')
        print(state)
        ZIP.zipfinder(str(city), str(state))
    elif com.lower() == "dist":
        firstzip = input('Enter the first ZIP Code: ')
        print(firstzip)
        secondzip = input('Enter the second ZIP Code: ')
        print(secondzip)
        ZIP.distination(int(firstzip), int(secondzip))
    elif com.lower() == 'end':
        print('Done')
    else:
        print('Такой команды нет!')
