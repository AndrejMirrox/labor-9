#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    # Source Dictionary
    school = {
        '1а': 22,
        '1б': 23,
        '1в': 25,
        '3а': 30,
        '3е': 24,
        '7в': 27,
        '10в': 17,
        '9а': 31,
        '3д': 24,
    }

    # Infinite Command Request Loop
    while True:
        command = input("Enter command:")
        if command == "change":
            while True:
                cc = input("Enter class you want change the num of students: ")
                nn = input("Enter the number of students students: ")
                if cc in school:
                    school[cc] = nn
                    break
                else:
                    print("This class does not exist")
            print(school)

        elif command == "delete":
            while True:
                cc = input("Enter the disbanded class: ")
                if cc in school:
                    school.pop(cc)
                    break
                else:
                    print("This class does not exist")
            print(school)

        elif command == "add":
            while True:
                cc = input("Enter new class: ")
                nn = input("Enter number of students: ")
                if cc in school:
                    print("This class already exist")
                else:
                    school[cc] = nn
                break
            print(school)
            
        elif command == "count":
            summa = 0
            for i in school:
                summa += int(school.get(i))
            print (summa)

        elif command == "exit":
            break

        else:
            print("Wrong command!")
