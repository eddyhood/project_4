import db
import utils


def register_employee():
    """Register a new employee"""
    utils.clear_screen()
    while True:
        print('===========  Register New Employees Here!  ===========')
        get_first_name = input('Enter First Name: ')
        get_last_name = input('Enter Employee\'s Last Name: ')
        print('You\'ve entered {} {} as the employee\'s name.'
              .format(get_first_name, get_last_name))
        confirm = input('Is this correct? Y/n: ').upper()
        if confirm == 'Y':
            db.Employee.create(
                            first_name=get_first_name,
                            last_name=get_last_name
                            )
            utils.clear_screen()
            print('You have successfully registered an employee!')
            break
        else:
            utils.clear_screen()
            print('Please enter the correct name.')
