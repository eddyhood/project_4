from collections import OrderedDict

import add
import employees
import search
import utils


def main_menu():
    """Show the menu to users"""
    utils.clear_screen()
    menu_choice = None
    while menu_choice != 'Q':
        print('========  Welcome to the Dunder Mifflin Worklog  ========\n')
        print('Enter "q" to quit.\n')
        for key, value in main.items():
            print('[{}] {}'.format(key, value.__doc__))
        menu_choice = input('\nChoose an option: ').upper().strip()

        if menu_choice in main:
            main[menu_choice]()


def search_menu():
    """Serach a log entry"""
    utils.clear_screen()
    choice = None
    while choice is None:
        print('==============  Search for a Prior Log  ==============\n')
        for key, value in search.items():
            print('[{}] {}'.format(key, value.__doc__))
        choice = input('Choose an option: ').upper().strip()

        if choice in search:
            search[choice]()


main = OrderedDict([
    ('R', employees.register_employee),
    ('A', add.add_log),
    ('S', search_menu),
])


search = OrderedDict([
    ('E', search.search_employee),
    ('D', search.search_date),
    ('R', search.search_date_range),
    ('T', search.search_time),
    ('P', search.search_phrase),

])
