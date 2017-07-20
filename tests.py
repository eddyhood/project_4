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
        """Test to see if valide date is converted to UTC"""
        self.assertTrue(utils.utc_date('12/31/2017'))

    def test_valid_date(self):
        """Test to see if a non-existant date thows ValueError"""
        self.assertRaises(ValueError, utils.utc_date, '12/32/2017')

    def test_utc_false_date(self):
        """Test to see if invalud date format throws TypeError"""
        self.assertRaises(TypeError, utils.utc_date, 12/31/2017)


class TestEdits(unittest.TestCase):
    def setUp(self):
        """Set up a log to be used in followin unit tests"""
        self.log = db.WorkLog.create(
                                     task_owner=1,
                                     task_name='$3$3$3',
                                     task_date='12/31/2017',
                                     task_time=50,
                                     task_notes='Fake notes')

    @patch('utils.get_input', return_value='$4$4$4')
    def test_edit_log_name(self, new_name):
        """Test to see if user can edit a log name"""
        utils.edit_log_name(self.log)
        self.assertTrue(db.WorkLog.get(task_name='$4$4$4'))

    @patch('utils.get_input', return_value='10/1/2017')
    def test_edit_log_date(self, new_date):
        """Test to see if user can edit a log date"""
        utils.edit_log_date(self.log)
        self.assertEqual(self.log.task_date, '10/1/2017')

    @patch('utils.get_input', return_value=100)
    def test_edit_log_time(self, new_time):
        """Test to see if user can edit a log time"""
        utils.edit_log_time(self.log)
        self.assertEqual(self.log.task_time, 100)

    @patch('utils.get_input', return_value='Extra Fake Note')
    def test_edit_log_note(self, new_note):
        """Test to see if user can edit a log note"""
        utils.edit_log_note(self.log)
        self.assertEqual(self.log.task_notes, 'Extra Fake Note')

    def test_work_log_header(self):
        """Test that header returns nothing, just a print statement"""
        self.assertFalse(utils.work_log_header())

    @patch('utils.get_input', return_value='1')
    def test_edit_log_selector(self, selector):
        """Test to see if user can choose a log to edit"""
        utils.edit_log(self.log)
        self.assertTrue(self.log)

    def tearDown(self):
        self.log.delete_instance()


class TestAdd(unittest.TestCase):

    @patch('utils.get_input', return_value='1')
    @patch('utils.get_input', return_value='Y$98$321')
    @patch('utils.get_input', return_value='12/31/2017')
    @patch('utils.get_input', return_value=50)
    @patch('utils.get_input', return_value='Fake Note')
    def test_add_log(self, id, name, date, time, note):
        """Test to see if all lines of code execute in step one of add logs"""
        self.assertFalse(add.add_log())


class TestEmployee(unittest.TestCase):

    @patch('utils.get_input', return_value='Fake$$$')
    @patch('utils.get_input', return_value='Name')
    @patch('utils.get_input', return_value='n')
    def test_get_employee(self, first_name, last_name, choice):
        """Test to see if all lines of code execute in step one of add emp"""
        self.assertFalse(employees.get_employee())

    @patch('utils.get_input', return_value='Y')
    def test_register_employee(self, input):
        """Test to see if employee gets added to database"""
        employees.register_employee('3$198##!', '3$198##!')
        check_add = db.Employee.get(first_name='3$198##!')
        self.assertTrue(check_add)

    def test_remove_employee(self):
        """Test to see if employee gets removed from database"""
        get_employee = db.Employee.get(first_name='3$198##!')
        del_employee = get_employee.delete_instance()
        self.assertTrue(del_employee)


class TestSearch(unittest.TestCase):

    def setUp(self):
        """Set up logs for the following unittests"""
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
    """Test that you can return to menu from employee search"""
    def test_leave_search_employees(self, input):
        self.assertFalse(search.search_employee())

    @patch('utils.get_input', return_value='M')
    def test_leave_search_date(self, input):
        """Test that you can return to menu from date search"""
        self.assertFalse(search.search_date())

    @patch('utils.get_input', return_value='M')
    def test_leave_search_time(self, input):
        """Test that you can return to menu from time search"""
        self.assertFalse(search.search_time())

    @patch('utils.get_input', return_value='M')
    def test_leave_search_phrase(self, input):
        """Test that you can return to menu from phrase search"""
        self.assertFalse(search.search_phrase())

    @patch('utils.get_input', return_value='M')
    def test_leave_display_options(self, input):
        """Test that all lines of code run in range search"""
        log_results = [self.fake_log_1, self.fake_log_2]
        self.assertFalse(search.display_options(log_results))

    def tearDown(self):
        """Tear down fake logs"""
        self.fake_log_1.delete_instance()
        self.fake_log_2.delete_instance()


class TestMenus(unittest.TestCase):

    @patch('utils.get_input', return_value='Q')
    """Test that you can quit the program"""
    def test_quit_program(self, input):
        self.assertFalse(menus.main_menu())

    @patch('utils.get_input', return_value='M')
    def test_quit_search_menu(self, input):
        """Test that you can quit the search program"""
        self.assertFalse(menus.search_menu())


if __name__ == '__main__':
    unittest.main()
