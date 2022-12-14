#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    # Dictionary with keys "numbers" and values "words"
    first_dict = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five'
    }

    # Using the .items function
    dict_items = first_dict.items()

    # Creating a new dictionary in which keys and values are changed
    new_dict = {v: k for k, v in dict_items}

    # Output
    print(new_dict)
