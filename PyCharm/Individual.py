#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import date, datetime

if __name__ == '__main__':
    # Список работников.
    people = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запрос команды
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о работнике.
            name = input("Фамилия и инициалы? ")
            post = input("Телефон? ")
            #year = input("Дата рождения? ")

            #year = date(int(year[2]), int(year[1]), int(year[0]))
            year = input("Введите дату рождения (гггг.мм.дд): ")
            year = year.split(".")
            year = date(int(year[0]), int(year[1]), int(year[2]))


            # Создать словарь.
            man = {
                'name': name,
                'tel': post,
                'date': year,
            }

            # Добавить словарь в список.
            people.append(man)
            # Отсортировать список в случае необходимости.
            if len(people) > 1:
                people.sort(key=lambda item: item.get('tel', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 20
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                    "№",
                    "Ф.И.О.",
                    "Телефон",
                    "Год рождения"
                )
            )
            print(line)

            # Вывести данные о всех сотрудниках.
            for idx, man in enumerate(people, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                        idx,
                        man.get('name', ''),
                        man.get('tel', ''),
                        str(man.get('date', ''))
                    )
                )
            print(line)

        elif command.startswith('select'):

            # Разбить команду на части.
            parts = command.split(' ', maxsplit=1)
            # Получить имя.
            period = parts[1]
            count = 0
            # Проверить сведения работников из списка.
            for man in people:
                if man.get('name', period).lower() == period.lower():
                    count += 1
                    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                        '-' * 4,
                        '-' * 30,
                        '-' * 20,
                        '-' * 12
                    )
                    print(line)
                    print(
                        '| {:^4} | {:^30} | {:^20} | {:^12} |'.format(
                            "№",
                            "Ф.И.О.",
                            "Телефон",
                            "Год рождения"
                        )
                    )
                    print(line)
                    print(
                        '| {:>4} | {:<30} | {:<20} | {:>12} |'.format(
                            count,
                            man.get('name', ''),
                            man.get('tel', ''),
                            str(man.get('date', 0))
                        )
                    )
                    print(line)


                # Если счетчик равен 0, то работники не найдены.
            if count == 0:
                print("Люди с заданным именем не найдены.")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить человека;")
            print("list - вывести список людей;")
            print("select <имя> - запросить людей с этим именем;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
