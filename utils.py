"""Stores functions that are used repeatedly across the entire app"""
import datetime
import os

import pytz


def clear_screen():
    """Function for clearing the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def delete_log(log):
    """Delete a log entry"""
    clear_screen()
    print('==============  You\'re Deleting The Following Log ==============')
    log_data(log)
    choice = get_input('Are you sure? Y/n:')
    if choice.upper().strip() == 'Y':
        log.delete_instance()
        clear_screen()
        print('***Your log was deleted.\n')
        get_input('Press any key to return to main menu: ')
        clear_screen()

    else:
        clear_screen()
        print('***Your log was NOT deleted.\n')
        input('Press any key to return to main menu: ')
        clear_screen()


def edit_log(log):
    """Edit a log entry"""
    # get_log = db.Worklog.get().where(db.Worklog.id == log.id)
    clear_screen()
    print('==============  You\'re Editing The Following Log ==============')
    log_data(log)
    while True:
        try:
            get_choice = get_input('\nEnter a number to edit: ')
            choice = int(get_choice)
            # Edit the task name
            if choice == 1:
                edit_log_name(log)
                break
            # Edit the task date
            elif choice == 2:
                edit_log_date(log)
                break
            # Edit the task time
            elif choice == 3:
                edit_log_time(log)
                break
            # Edit the task notes
            elif choice == 4:
                edit_log_note(log)
                break
            else:
                raise ValueError
        except:
            print('\nError.  Please enter one of the available options.')


def edit_log_name(log):
    """Allows user to edit the name of a stored log"""
    get_name = get_input('\nEnter a new task name: ')
    log.task_name = get_name
    log.save()
    clear_screen()
    show_edited_log(log)


def edit_log_date(log):
    """Allows user to edit the date of a stored log"""
    try:
        get_date = get_input('\nEnter a new date as MM/DD/YYY: ')
        utc_date(get_date)
    except ValueError:
        print('\nError.  Enter a valid date as MM/DD/YYYY')
    else:
        log.task_date = get_date
        log.save()
        clear_screen()
        show_edited_log(log)


def edit_log_time(log):
    """Allows user to edit the time of a stored log"""
    try:
        get_time = get_input('\nEnter a new time: ')
        time_int = int(get_time)
    except ValueError:
        print('\nError. Enter a valid number.')
    else:
        log.task_time = time_int
        log.save()
        clear_screen()
        show_edited_log(log)


def edit_log_note(log):
    """Allows user to edit the notes of a stored log"""
    get_note = get_input('\nEnter a new note: ')
    log.task_notes = get_note
    log.save()
    clear_screen()
    show_edited_log(log)


def show_edited_log(log):
    """Shows user the updated log after edits have been made"""
    clear_screen()
    print('==============  Your Changes Have Been Saved! ==============')
    log_data(log)
    get_input('Press any key to return to search menu')
    clear_screen()


def log_data(log):
    """Shows a current view of the log being updated"""
    print('#1 - Task Name: {}'.format(log.task_name))
    print('#2 - Task Date: {}'.format(log.task_date))
    print('#3 - Task Time: {}'.format(log.task_time))
    print('#4 - Task Note: {}'.format(log.task_notes))


def get_input(text):
    '''Removes user input from functions so that unittest runs cleaner'''
    return input(text)


def get_start_date():
    """Retrieves start date for the date range search"""
    start_date = None
    while start_date != 'M':
        try:
            print('\n[M]enu or enter a START DATE as MM/DD/YYYY')
            start_date = input('Choose an Option: ')
            if start_date.upper().strip() == 'M':
                clear_screen()
                start_date = None
                break
            else:
                utc_date(start_date)
        except ValueError:
            print('\nError. Enter a valid date as MM/DD/YYYY')
        else:
            return start_date
            break


def get_end_date():
    """Retrieves a date from the user, checks its validity, and returns it
    to a search function that looks up logs by date range"""
    end_date = None
    while end_date != 'M':
        try:
            print('\n[M]enu or enter am END DATE as MM/DD/YYYY')
            end_date = input('Choose an Option: ')
            if end_date.upper().strip() == 'M':
                clear_screen()
                end_date = None
                break
            else:
                utc_date(end_date)
        except ValueError:
            print('\nError. Enter a valid date as MM/DD/YYYY')
        else:
            return end_date
            break


def utc_date(date):
    """Convert a date from user into UTC time"""
    date = datetime.datetime.strptime(date, "%m/%d/%Y")
    utc_date = date.astimezone(pytz.utc)
    return(utc_date)


def work_log_header():
    """Displays a header in the worklog section"""
    clear_screen()
    print('================  Add a New Worklog Here  ================\n')
