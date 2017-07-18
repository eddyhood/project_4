"""Stores functions that are used repeatedly across the entire app"""
import datetime
import os

import pytz

import menus


def clear_screen():
    """Function for clearing the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def delete_log(log):
    """Delete a log entry"""
    clear_screen()
    print('==============  You\'re Deleting The Following Log ==============')
    print('#1 - Task Name: {}'.format(log.task_name))
    print('#2 - Task Date: {}'.format(log.task_date))
    print('#3 - Task Time: {}'.format(log.task_time))
    print('#4 - Task Note: {}'.format(log.task_notes))

    choice = input('Are you sure? Y/n:')
    if choice == 'y':
        log.delete_instance()
    else:
        print('The log was not deleted')


def confirm_edits(log):
    clear_screen()
    print('==============  Confirm & Save ==============')
    print('Review Your Changes Below: ')
    print('#1 - Task Name: {}'.format(log.task_name))
    print('#2 - Task Date: {}'.format(log.task_date))
    print('#3 - Task Time: {}'.format(log.task_time))
    print('#4 - Task Note: {}'.format(log.task_notes))
    confirm = input('Want to save your changes?  Y/n: ').upper().strip()

    if confirm == 'Y':
        log.save()
        clear_screen()
        print('Your changes have been saved!')
        input('Press any key to return to main menu: ')
        menus.main_menu()
    else:
        print('You\'r changs were not saved.')


def edit_log(log):
    """Edit a log entry"""
    # get_log = db.Worklog.get().where(db.Worklog.id == log.id)
    clear_screen()
    print('==============  You\'re Editing The Following Log ==============')
    print('#1 - Task Name: {}'.format(log.task_name))
    print('#2 - Task Date: {}'.format(log.task_date))
    print('#3 - Task Time: {}'.format(log.task_time))
    print('#4 - Task Note: {}'.format(log.task_notes))

    while True:
        try:
            choice = int(input('\nEnter a number to edit: '))
            # Edit the task name
            if choice == 1:
                get_name = input('\nEnter a new task name: ')
                log.task_name = get_name
                confirm_edits(log)
            # Edit the task date
            elif choice == 2:
                while True:
                    try:
                        get_date = input('\nEnter a new date as MM/DD/YYY: ')
                        utc_date(get_date)
                    except ValueError:
                        print('\nError.  Enter a valid date as MM/DD/YYYY')
                    else:
                        log.task_date = get_date
                        confirm_edits(log)
                        break
            # Edit the task time
            elif choice == 3:
                while True:
                    try:
                        get_time = int(input('\nEnter a new time: '))
                    except ValueError:
                        print('\nError. Enter a valid number.')
                    else:
                        log.task_time = get_time
                        confirm_edits(log)
                        break
            # Edit the task notes
            elif choice == 4:
                get_note = input('\nEnter a new note: ')
                log.task_notes = get_note
                confirm_edits(log)
            else:
                raise ValueError
        except:
            print('\nError.  Please enter one of the available options.')
        else:
            break


def utc_date(date):
    """Convert a date from user into UTC time"""
    date = datetime.datetime.strptime(date, "%m/%d/%Y")
    utc_date = date.astimezone(pytz.utc)
    return(utc_date)


def work_log_header():
    clear_screen()
    print('================  Add a New Worklog Here  ================\n')
