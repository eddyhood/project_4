import sys
from collections import OrderedDict

import add
import employees
import search
import utils


def main_menu():
    """Show the menu to users"""
    main = OrderedDict([
                       ('R', employees.register_employee),
                       ('A', add.add_log),
                       ('S', search_menu),
                       ])
    utils.clear_screen()
    menu_choice = None
    while menu_choice != 'Q':
        print('========  Welcome to the Dunder Mifflin Worklog  ========\n')
        print('Enter "Q" to Quit.\n')
        for key, value in main.items():
            print('[{}] {}'.format(key, value.__doc__))
        menu_choice = utils.get_input('\nChoose an option: ').upper().strip()
        if menu_choice in main:
            main[menu_choice]()
        else:
            utils.clear_screen()


def search_menu():
    """Serach a log entry"""
    search_options = OrderedDict([
                         ('E', search.search_employee),
                         ('D', search.search_date),
                         ('R', search.search_date_range),
                         ('T', search.search_time),
                         ('P', search.search_phrase),
                         ])
    utils.clear_screen()
    choice = None
    while choice != 'M':
        print('==============  Search for a Prior Log  ==============\n')
        print('Enter "Q" to quit.\n')
        for key, value in search_options.items():
            print('[{}] {}'.format(key, value.__doc__))
        choice = utils.get_input('Choose an option: ').upper().strip()

        if choice in search_options:
            search_options[choice]()
        else:
            utils.clear_screen()
