"""This module holds all of the methods necessary to search for logs
in the database."""

import db
import utils


def search_employee():
    """Search by employee"""
    utils.clear_screen()
    print('==========  Search Logs by Employee ==========\n')
    get_employees = db.Employee.select()
    row_num = 0
    for staff in get_employees:
        row_num += 1
        get_logs = db.WorkLog.select().where(db.WorkLog.task_owner
                                             == staff.id).count()
        print('#{}. {}, {}: {} log(s)'
              .format(staff.id, staff.last_name, staff.first_name, get_logs))
    choice = None
    while choice != 'Q':
        try:
            print('\n[M]ain Menu or Enter Employee id# to view logs')
            choice = (input('Choose an Option: '))
            if choice.upper().strip() == 'M':
                utils.clear_screen()
                break
            else:
                check_int = int(choice)
                if db.WorkLog.get(db.WorkLog.task_owner==check_int):
                    logs = db.WorkLog.select().where(db.WorkLog.task_owner==check_int)
                    display_options(logs)
                else:
                    raise Exception
        except Exception:
            print('Error.  Enter the employee id# to view logs.')
        else:
            break


def search_date():
    """Search by specific date"""
    utils.clear_screen()
    print('===========  Search Logs by Date ===========\n')
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
    choice = None
    while choice != 'Q':
        try:
            print('\n[M}ain Menu or Enter # to view logs by date')
            choice = (input('Choose an Option: '))
            if choice.upper().strip() == 'M':
                utils.clear_screen()
                break
            else:
                check_int = int(choice)
                if check_int in range(0, row_num+1):
                    logs = db.WorkLog.select().where(db.WorkLog.task_date==
                                                     date_options[check_int])
                    display_options(logs)
                else:
                    raise Exception
        except Exception:
            print('\nError.  Enter the date# to view logs for that date.')
        else:
            break


def search_date_range():
    """Search by date range"""
    utils.clear_screen()
    print('==========  Search Logs by Date Range  =========\n')
    try:
        start_date = utils.get_start_date()
        if start_date:
            end_date = utils.get_end_date()
            if end_date:
                # Query logs that fit the daterange
                logs = db.WorkLog.select()\
                .where(start_date<=db.WorkLog.task_date<=end_date)\
                .order_by(db.WorkLog.task_date)
                # Send logs to display function
                display_options(logs)
            else:
                pass
        else:
            pass
    except Exception:
        print('Hmmm, something went wrong.')


def search_time():
    """Search by time"""
    utils.clear_screen()
    print('==========  Search Logs by Date Range  =========\n')
    get_time = None
    while get_time != 'M':
        try:
            print('[M]enu or enter amt of time.  i.e. 50 for 50 minutes.')
            get_time = (input('Choose an Option:'))
            if get_time.upper().strip() == 'M':
                utils.clear_screen()
                break
            else:
                is_int = int(get_time)
        except ValueError:
            print('\nError. Please enter a number.  i.e. 50 for 50 minutes')
        else:
            if db.WorkLog.select().where(db.WorkLog.task_time==get_time):
                # Query database for logs that match time
                get_logs = db.WorkLog.select()\
                .where(db.WorkLog.task_time==get_time)
                # Send logs to display function
                display_options(get_logs)
                break
            else:
                print('Error. There are no logs that match that time.')


def search_phrase():
    """Search by phrase"""
    utils.clear_screen()
    print('===========  Search Logs by Phrase  ===========\n')
    get_phrase = None
    while get_phrase != 'M':
        try:
            print('[M]enu or enter phrase to serach')
            get_phrase = input('Choose an Option: ')
            if get_phrase.upper().strip() == 'M':
                utils.clear_screen()
                break
            else:
                # Query database for logs that match phrase
                get_logs = db.WorkLog.select()\
                .where(db.WorkLog.task_name.contains(get_phrase) \
                       or db.WorkLog.task_notes.contains(get_phrase))
                # Send matching logs to dispaly function
                if get_logs:
                    display_options(get_logs)
                else:
                    raise ValueError
        except ValueError:
            print('\nError.  That phrase is not found.\n')


def display_options(log_results):
    utils.clear_screen()
    print('=======  Successful Search! You\'r Results Are: =======')
    log_list = [log for log in log_results]
    display_result(log_list[0])
    current_count = 1
    total_count = len(log_list)

    # display menu options
    choice = None
    while choice != 'M':
        print('\nResult {} of {}'.format(current_count, total_count))
        print('\n[N]ext, [P]revious, [E]dit, [D]elete, [M]enu')
        choice = input('Choose an Option: ').upper().strip()
        # Show total results as {} of {}

        # Get user choice
        try:
            # If choice is 'N', show the next log if available.
            if choice == 'N':
                try:
                    utils.clear_screen()
                    if current_count < total_count:
                        current_count += 1
                        display_result(log_list[current_count-1])
                    else:
                        display_result(log_list[current_count-1])
                except Exception:
                    print('Error.  There are no more logs to view.')
            # if choice is 'P', show the previous log if available
            elif choice == 'P':
                try:
                    if current_count > 1:
                        utils.clear_screen()
                        current_count -= 1
                        display_result(log_list[current_count-1])
                    else:
                        display_result(log_list[current_count-1])
                except Exception:
                    print('Error.  There are no more logs to view')
            # if choice is 'E' launch the edit function
            elif choice == 'E':
                utils.edit_log(log_list[current_count-1])
                break
            # if choice is 'D' launch the delete function
            elif choice == 'D':
                utils.delete_log(log_list[current_count-1])
                break
            # if choice is 'M', clear screen and left default menu loop play
            elif choice == 'M':
                utils.clear_screen()
                break
            else:
                raise ValueError
        except ValueError:
            print('Error.  Please enter a valid option.')


def display_result(log):
    """displays results of a search function"""
    utils.clear_screen()
    print('=======  Successful Search! You\'r Results Are: =======')
    print('Task Name: {}'.format(log.task_name))
    print('Task Date: {}'.format(log.task_date))
    print('Task Time: {}'.format(log.task_time))
    print('Task Note: {}'.format(log.task_notes))
