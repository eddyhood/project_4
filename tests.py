import unittest
from unittest.mock import patch

import add
import db
import employees
import menus
import search
import utils


class TestUtils(unittest.TestCase):

    def test_utc_date(self):
        self.assertTrue(utils.utc_date('12/31/2017'))

    def test_valid_date(self):
        self.assertRaises(ValueError, utils.utc_date, '12/32/2017')

    def test_utc_false_date(self):
        self.assertRaises(TypeError, utils.utc_date, 12/31/2017)


class TestEdits(unittest.TestCase):
    def setUp(self):
        self.log = db.WorkLog.create(
                                     task_owner=1,
                                     task_name='$3$3$3',
                                     task_date='12/31/2017',
                                     task_time=50,
                                     task_notes='Fake notes')

    @patch('utils.get_input', return_value='$4$4$4')
    def test_edit_log_name(self, new_name):
        utils.edit_log_name(self.log)
        self.assertTrue(db.WorkLog.get(task_name='$4$4$4'))

    @patch('utils.get_input', return_value='10/1/2017')
    def test_edit_log_date(self, new_date):
        utils.edit_log_date(self.log)
        self.assertEqual(self.log.task_date, '10/1/2017')

    @patch('utils.get_input', return_value=100)
    def test_edit_log_time(self, new_time):
        utils.edit_log_time(self.log)
        self.assertEqual(self.log.task_time, 100)

    @patch('utils.get_input', return_value='Extra Fake Note')
    def test_edit_log_note(self, new_note):
        utils.edit_log_note(self.log)
        self.assertEqual(self.log.task_notes, 'Extra Fake Note')

    def test_work_log_header(self):
        self.assertFalse(utils.work_log_header())


    def tearDown(self):
        self.log.delete_instance()



class TestAdd(unittest.TestCase):

    @patch('menus.main_menu', return_value='A')
    @patch('utils.get_input', return_value='Y')
    def test_add_log(self, input1, input2):
        add.save_worklog(1,'14$56', '12/31/2017', 50, 'Fake Note')
        check_add = db.WorkLog.get(task_name='14$56')
        self.assertTrue(check_add)

    @patch('utils.get_input', return_value='n')
    def test_add_summary(self, input):
        self.assertFalse(add.add_summary(1,'14$56', '12/31/2017', 50, 'Fake Note'))

    @patch('utils.get_input', return_value='Y')
    def test_delete_log(self, input1):
        delete_fake_log = utils.delete_log(db.WorkLog.get(task_name='14$56'))
        self.assertFalse(delete_fake_log)


class TestEmployee(unittest.TestCase):

    @patch('utils.get_input', return_value='Fake$$$')
    @patch('utils.get_input', return_value='Name')
    @patch('utils.get_input', return_value='n')
    def test_get_employee(self, first_name, last_name, choice):
        self.assertFalse(employees.get_employee())


    @patch('utils.get_input', return_value='Y')
    def test_register_employee(self, input):
        employees.register_employee('3$198##!', '3$198##!')
        check_add = db.Employee.get(first_name='3$198##!')
        self.assertTrue(check_add)

    def test_remove_employee(self):
        get_employee = db.Employee.get(first_name='3$198##!')
        del_employee = get_employee.delete_instance()
        self.assertTrue(del_employee)

class TestSearch(unittest.TestCase):

    def setUp(self):
        self.fake_log_1 = db.WorkLog.create(
                                     task_owner=1,
                                     task_name='$?590th$#',
                                     task_date='12/31/2017',
                                     task_time=50,
                                     task_notes='Fake notes')

        self.fake_log_2 = db.WorkLog.create(
                                     task_owner=1,
                                     task_name='$?590th$9',
                                     task_date='12/31/2017',
                                     task_time=50,
                                     task_notes='Fake notes')

    @patch('utils.get_input', return_value='M')
    def test_leave_search_employees(self, input):
        self.assertFalse(search.search_employee())

    @patch('utils.get_input', return_value='M')
    def test_leave_search_date(self, input):
        self.assertFalse(search.search_date())

    @patch('utils.get_input', return_value='M')
    def test_leave_search_time(self, input):
        self.assertFalse(search.search_time())

    @patch('utils.get_input', return_value='M')
    def test_leave_search_phrase(self, input):
        self.assertFalse(search.search_phrase())

    @patch('utils.get_input', return_value='M')
    def test_leave_display_options(self, input):
        log_results = [self.fake_log_1, self.fake_log_2]
        self.assertFalse(search.display_options(log_results))

    def tearDown(self):
        self.fake_log_1.delete_instance()
        self.fake_log_2.delete_instance()


class TestMenus(unittest.TestCase):

    @patch('utils.get_input', return_value='Q')
    def test_quit_program(self, input):
        self.assertFalse(menus.main_menu())

    @patch('utils.get_input', return_value='M')
    def test_quit_program(self, input):
        self.assertFalse(menus.search_menu())

if __name__ == '__main__':
    unittest.main()
