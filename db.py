#!/usr/bin/env python3

"""
Worklog is a log tracking system by employee.

Created: July 2017
Author: Eddy Hood

"""
import datetime

from peewee import *

import menus

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


if __name__ == '__main__':
    initialize()
    menus.main_menu()
