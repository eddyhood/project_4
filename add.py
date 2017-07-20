"""Module containing the functions for adding logs to the worklog"""
import db
import utils


def add_log():
    """Add a log entry"""
    utils.work_log_header()
    # Assign a task to an employee in the database
    while True:
        try:
            print('Which Employee Performed the Task?')
            for employee in db.Employee.select():
                print('#{}) {} {}'.format(employee.id, employee.first_name,
                                          employee.last_name))
            choice = utils.get_input('\nEnter the employee ID: ')
            get_employee = int(choice)
            if not db.Employee.get(db.Employee.id == get_employee):
                raise Exception
        except Exception:
            utils.clear_screen()
            print('\n*** Error. Please enter a valid employee id #.*** ')
        else:
            break

    # Assign a task name to the log
    utils.work_log_header()
    get_task_name = utils.get_input('Enter a task name: ')

    # Assign a date to the log & test to make sure it's a valid date
    utils.work_log_header()
    while True:
        try:
            get_task_date = utils.get_input('Enter task date as MM/DD/YYYY: ')
            utils.utc_date(get_task_date)
        except ValueError:
            print('Error.  Please enter a valid date as MM/DD/YYYY.')
        else:
            break

    # Assign a time to the log
    utils.work_log_header()
    while True:
        try:
            time_choice = utils.get_input('Enter task time in minutes: ')
            get_task_time = int(time_choice)
        except ValueError:
            print("Error.  Enter a number only.  i.e. 50 for 50 minutes.")
        else:
            break

    # Assign a note to the log
    utils.work_log_header()
    get_task_notes = utils.get_input('Enter task notes: ')

    add_summary(get_employee, get_task_name, get_task_date, get_task_time,
                get_task_notes)


def add_summary(employee, name, date, time, note):
    # Print summary and allow user to confirm before saving to database
    utils.clear_screen()
    print('\n================  Log Summary:  ================')
    print('\nEmployee: {} {}'
          .format(db.Employee.get(db.Employee.id == employee).first_name,
                  db.Employee.get(db.Employee.id == employee).last_name))
    print('Task Name: {}'.format(name))
    print('Task Date: {}'.format(date))
    print('Task Time: {}'.format(time))
    print('Task Note: {}'.format(note))
    save_worklog(employee, name, date, time, note)


def save_worklog(employee, name, date, time, note):
    choice = utils.get_input('\nReady to save it? Y/n: ')
    if choice.upper() == 'Y':
        db.WorkLog.create(
                task_owner=employee,
                task_name=name,
                task_date=date,
                task_time=time,
                task_notes=note
                )
        utils.clear_screen()
        print('You have successfully added a worklog.\n')
        utils.get_input('Press any key to return to main menu: ')
        utils.clear_screen()
    else:
        utils.clear_screen()
        print('Your log was not saved.')
        utils.get_input('Press any key to return to main menu: ')
        utils.clear_screen()
