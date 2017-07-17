"""This module holds all of the methods necessary to search for logs
in the database."""

import db
import utils

import menus


def search_employee():
    """Search by employee"""
    utils.clear_screen()
    print('=============  Search Logs by Employee (Type Q to Quit)  =============\n')
    get_employees = db.Employee.select()
    for staff in get_employees:
        get_logs = db.WorkLog.select().where(db.WorkLog.task_owner
                                             == staff.id).count()
        print('#{}. {} {} - {} log(s)'
              .format(staff.id, staff.first_name, staff.last_name, get_logs))
    choice = None
    while choice != 'q':
        try:
            choice = int(input('\nEnter employee id# to view logs: '))
            if db.WorkLog.get(db.WorkLog.task_owner==choice):
                log_results = db.WorkLog.select().where(db.WorkLog.task_owner
                                                        == choice)
                display_options(log_results)
            else:
                raise Exception
        except Exception:
            print('Error.  Enter the employee id# to view logs.')
        else:
            break


def search_date():
    """Search by specific date"""
    utils.clear_screen()
    print('=============  Search Logs by Date  =============\n')
    get_logs = db.WorkLog.select()
    group_logs = get_logs.group_by(db.WorkLog.task_date)
    row_num = 0
    date_options = {}
    for log in group_logs:
        count_logs = get_logs.where(db.WorkLog.task_date
                                    == log.task_date).count()
        row_num += 1
        print('#{}: {} - {} log(s)'.format(row_num, log.task_date, count_logs))
        date_options[row_num] = log.task_date
    while True:
        try:
            choice = int(input('\nEnter number to view logs by date: '))
            if choice in range(0, row_num+1):
                get_logs = db.WorkLog.select().where(db.WorkLog.task_date
                                                     ==date_options[choice])
                display_options(get_logs)
            else:
                raise Exception
        except Exception:
            print('\nError.  Enter the date# to view logs for that date.')
        else:
            break


def search_date_range():
    """Search by date range"""
    utils.clear_screen()
    print('=============  Search Logs by Date Range =============\n')
    while True:
        try:
            start_date = input('Enter a start date as MM/DD/YYYY: ')
            utils.utc_date(start_date)
        except ValueError:
            print('\nError. Enter a valid date as MM/DD/YYYY')
        else:
            break

    while True:
        try:
            end_date = input('Enter an end date as MM/DD/YYYY: ')
            utils.utc_date(end_date)
        except ValueError:
            print('\nError. Enter a valid date as MM/DD/YYYY')
        else:
            break
    get_logs = db.WorkLog.select().where(start_date <= db.WorkLog.task_date
                                         <= end_date)
    display_options(get_logs)


def search_time():
    """Search by time"""
    utils.clear_screen()
    print('=============  Search Logs by Date Range =============\n')
    while True:
        try:
            get_time = int(input('Enter an amount of time to search:'))
        except ValueError:
            print('\nError. Please enter a number.  i.e. 50 for 50 minutes')
        else:
            if db.WorkLog.select().where(db.WorkLog.task_time==get_time):
                get_logs = db.WorkLog.select().where(db.WorkLog.task_time
                                                     ==get_time)
                display_options(get_logs)
            else:
                print('Error. There are no logs that match that time.')


def search_phrase():
    """Search by phrase"""
    utils.clear_screen()
    print('=============  Search Logs by Phrase =============\n')
    while True:
        try:
            get_phrase = input('Enter a phrase to search: ')
            get_logs = db.WorkLog.select().where(db.WorkLog.task_name.
                                                 contains(get_phrase) or
                                                 db.WorkLog.task_notes.
                                                 contains(get_phrase))
            if get_logs:
                display_options(get_logs)
            else:
                raise Exception
        except Exception:
            print('Error.  That phrase is not found.')
        else:
            break


def display_options(log_results):
    utils.clear_screen()
    print('=======  Successful Search! You\'r Results Are: =======')
    log_list = []
    for log in log_results:
        log_list.append(log)
    display_result(log_list[0])
    display_count = 1
    total = len(log_list)

    # display menu options
    choice = None
    while choice != 'M':
        try:
            print('\nResult {} of {}'.format(display_count, total))

            # Get user choice
            print('\n[N]ext, [P]revious, [E]dit, [D]elete, [M]enu')
            choice = input('Choose an Option: ').upper().strip()

            # Handle user's choice
            if choice == 'N':
                try:
                    utils.clear_screen()
                    if display_count < total:
                        display_count += 1
                        display_result(log_list[display_count-1])
                    else:
                        display_result(log_list[display_count-1])
                except Exception:
                    print('Error.  There are no more logs to view.')
                    continue
            elif choice == 'P':
                try:
                    if display_count > 1:
                        utils.clear_screen()
                        display_count -= 1
                        display_result(log_list[display_count-1])
                    else:
                        display_result(log_list[display_count-1])
                except Exception:
                    print('Error.  There are no more logs to view')
                    continue
            elif choice == 'E':
                utils.edit_log()
            elif choice == 'D':
                utils.delete_log()
            elif choice == 'M':
                utils.clear_screen()
            else:
                raise ValueError
        except ValueError:
            print('Error.  Please enter a valid option.')
            continue
        else:
            continue


def display_result(log):
    """displays results of a search function"""
    utils.clear_screen()
    print('=======  Successful Search! You\'r Results Are: =======')
    print('Task Name: {}'.format(log.task_name))
    print('Task Date: {}'.format(log.task_date))
    print('Task Time: {}'.format(log.task_time))
    print('Task Note: {}'.format(log.task_notes))
