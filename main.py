import json


def main():

    # Путь к файлу
    file_path = 'data.json'

    help_text = ('__Навигация__\n'
                 '0: Выход\n'
                 '1: Показать справочник\n'
                 '2: Поиск по характеристикам\n'
                 '3: Загрузить данные\n'
                 '4: Удалить запить из справочника\n'
                 )

    while True:
        """ Запускаю бесконечный цикл, который позволяет не выключить программу
         и выполняет определенные действия в соответствии с help_text """

        print(help_text)
        command = input('Введите комманду: \n')

        if command == '0':
            break


        elif command == '1':
            with open(file_path, 'r', encoding='utf-8') as file:
                data: list = json.load(file)
                for i, element in enumerate(data):
                    print(f'{i} - {element["first_name"]} {element["last_name"]} phone: {element["phone"]}')


        elif command == '2':
            print('1 - Поиск по имени\n'
                  '2 - Поиск по телефону\n'
                  '3 - Поиск по имени и телефону')
            choice: str = input('По каким параметрам осуществлять поиск:')

            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            if choice == '1':
                name: str = input('Введите имя: \n')
                for i, element in enumerate(data):
                    if name in element['first_name'] or name in element['last_name'] or name in element['middle_name']:
                        print(f'{i} - {element["first_name"]} {element["last_name"]} phone: {element["phone"]}')

            elif choice == '2':
                phone: str = input('Введите телефон: \n')
                for i, element in enumerate(data):
                    if phone in element['phone'] or phone in element['mobile']:
                        print(f'{i} - {element["first_name"]} {element["last_name"]} phone: {element["phone"]}')

            elif choice == '3':
                name: str = input('Введите имя: \n')
                phone: str = input('Введите телефон: \n')
                for i, element in enumerate(data):
                    if (name in element['first_name'] or name in element['last_name'] or name in element['middle_name']
                            and phone in element['phone'] or phone in element['mobile']):
                        print(f'{i} - {element["first_name"]} {element["last_name"]} phone: {element["phone"]}')


        elif command == '3':
            w_n = input('Введите имя: \n')
            w_f = input('Введите фамилию: \n')
            w_o = input('Введите отчество: \n')
            w_org = input('Введите организацию: \n')
            w_phone = input('Введите телефон: \n')
            w_mobile = input('Введите мобильный: \n')

            json_data = {
                'first_name': w_n,
                'last_name': w_f,
                'middle_name': w_o,
                'organization': w_org,
                'phone': w_phone,
                'mobile': w_mobile
            }

            data = json.load(open(file_path, encoding='utf-8'))
            data.append(json_data)

            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)


        elif command == '4':
            index = int(input('Введите номер записи: \n')) - 1
            data = json.load(open(file_path, encoding='utf-8'))
            data.pop(index)
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
