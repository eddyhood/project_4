"""Stores functions that are used repeatedly across the entire app"""
import datetime
import os

import pytz


def clear_screen():
    """Function for clearing the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_results():
    """displays results of a search function"""
    pass


def utc_date(date):
    """Convert a date from user into UTC time"""
    date = datetime.datetime.strptime(date, "%m/%d/%Y")
    utc_date = date.astimezone(pytz.utc)
    return(utc_date)
