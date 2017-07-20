import db
import utils


def get_employee():
    """Register a new employee"""
    utils.clear_screen()
    print('===========  Register New Employees Here!  ===========')
    first_name = utils.get_input('Enter First Name: ')
    last_name = utils.get_input('Enter Employee\'s Last Name: ')
    print('You\'ve entered {} {} as the employee\'s name.'
          .format(first_name, last_name))
    confirm = utils.get_input('Is this correct? Y/n: ').upper()
    if confirm == 'Y':
        register_employee(first_name, last_name)
    else:
        utils.clear_screen()
        print('Please enter the correct name.')


def register_employee(first_name, last_name):
    """Register a new employee"""
    db.Employee.create(first_name=first_name, last_name=last_name)
    utils.clear_screen()
    print('***Your have successfully registered an employee.\n')
    utils.get_input('Press any key to return to main menu: ')
    utils.clear_screen()
