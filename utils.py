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
    print('Log to delete: {}'.format(log.task_name))
    choice = input('What shall I delete?')


def edit_log(log):
    """Edit a log entry"""
    print('Log to edit: {}'.format(log.task_name))
    choice = input('what shall I edit?')


def utc_date(date):
    """Convert a date from user into UTC time"""
    date = datetime.datetime.strptime(date, "%m/%d/%Y")
    utc_date = date.astimezone(pytz.utc)
    return(utc_date)


def work_log_header():
    clear_screen()
    print('================  Add a New Worklog Here  ================\n')
