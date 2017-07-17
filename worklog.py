#!/usr/bin/env python3

"""Contains all of the models used by Peewee"""
from collections import OrderedDict
import datetime

from peewee import *

import search_methods
import utils

db = SqliteDatabase('worklog.db')


class Employee(Model):
    """Creates an employee object"""
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)

    class Meta:
        database = db


class WorkLog(Model):
    """Creates a worklog object"""
    task_owner = ForeignKeyField(Employee, related_name='logs')
    task_name = CharField()
    task_date = DateField()
    task_time = IntegerField()
    task_notes = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def initialize():
    """Initializes database and creates new tables"""
    db.connect()
    db.create_tables([Employee, WorkLog], safe=True)


def register_employee():
    """Register a New Employee"""
    utils.clear_screen()
    while True:
        print('===========  Register New Employees Here!  ===========')
        get_first_name = input('Enter First Name: ')
        get_last_name = input('Enter Employee\'s Last Name: ')
        print('You\'ve entered {} {} as the employee\'s name.'
              .format(get_first_name, get_last_name))
        confirm = input('Is this correct? Y/n: ').upper()
        if confirm == 'Y':
            Employee.create(
                            first_name=get_first_name,
                            last_name=get_last_name
                            )
            utils.clear_screen()
            print('You have successfully registered an employee!')
            break
        else:
            utils.clear_screen()
            print('Please enter the correct name.')


def add_log():
    """Add a log entry"""
    utils.clear_screen()
    print('================  Add a New Worklog Here  ================\n')
    # Assign a task to an employee in the database
    while True:
        try:
            print('Which Employee Performed the Task?')
            for employee in Employee.select():
                print('#{}) {} {}'.format(employee.id, employee.first_name,
                                          employee.last_name))
            get_employee = int(input('\nEnter the employee ID: '))
            if not Employee.get(Employee.id == get_employee):
                raise Exception
        except Exception:
            print('\n*** Error. Please enter a valid employee id #.*** ')
        else:
            break

    # Assign a task name to the log
    utils.clear_screen()
    print('================  Add a New Worklog Here  ================\n')
    get_task_name = input('Enter a task name: ')

    # Assign a date to the log & test to make sure it's a valid date
    utils.clear_screen()
    print('================  Add a New Worklog Here  ================\n')
    while True:
        try:
            get_task_date = input('Enter task date as MM/DD/YYYY: ')
            utils.utc_date(get_task_date)
        except ValueError:
            print('Error.  Please enter a valid date as MM/DD/YYYY.')
        else:
            break

    # Assign a time to the log
    utils.clear_screen()
    print('================  Add a New Worklog Here  ================\n')
    while True:
        try:
            get_task_time = int(input('Enter task time in minutes: '))
        except ValueError:
            print("Error.  Enter a number only.  i.e. 50 for 50 minutes.")
        else:
            break

    # Assign a note to the log
    utils.clear_screen()
    print('================  Add a New Worklog Here  ================\n')
    get_task_notes = input('Enter task notes: ')

    # Print summary and allow user to confirm before saving to database
    utils.clear_screen()
    print('\n================  Log Summary:  ================')
    print('\nEmployee: {} {}'
          .format(Employee.get(Employee.id == get_employee).first_name,
                  Employee.get(Employee.id == get_employee).last_name))
    print('Task Name: {}'.format(get_task_name))
    print('Task Date: {}'.format(get_task_date))
    print('Task Time: {}'.format(get_task_time))
    print('Task Note: {}'.format(get_task_notes))

    choice = input('\nReady to save it? Y/n: ')
    if choice.upper() == 'Y':
        WorkLog.create(
                task_owner=get_employee,
                task_name=get_task_name,
                task_date=get_task_date,
                task_time=get_task_time,
                task_notes=get_task_notes
                )
        print('You have successfully added a worklog.\n')
    else:
        print('Alright.  Let\'s try that again.')


def menu_loop():
    """Show the menu to users"""
    utils.clear_screen()
    choice = None
    while choice != 'Q':
        print('========  Welcome to the Dunder Mifflin Worklog  ========\n')
        print('Enter "q" to quit.')
        for key, value in menu.items():
            print('[{}] {}'.format(key, value.__doc__))
        choice = input('Choose an option: ').upper().strip()

        if choice in menu:
            menu[choice]()


def search_menu():
    """Serach a log entry"""
    utils.clear_screen()
    choice = None
    while choice is None:
        print('==============  Search for a Prior Log  ==============\n')
        for key, value in search_menu.items():
            print('[{}] {}'.format(key, value.__doc__))
        choice = input('Choose an option: ')

        if choice in search_menu:
            search_menu[choice]()


def edit_log():
    """Edit a log entry"""
    pass


def delete_log():
    """Delete a log entry"""
    pass


menu = OrderedDict([
    ('R', register_employee),
    ('A', add_log),
    ('S', search_menu),
])

search_menu = OrderedDict([
    ('E', search_methods.search_employee),
    ('D', search_methods.search_date),
    ('R', search_methods.search_date_range),
    ('T', search_methods.search_time),
    ('P', search_methods.search_phrase),

])

if __name__ == '__main__':
    initialize()
    menu_loop()
