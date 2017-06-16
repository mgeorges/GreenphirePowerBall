import unittest
from unittest import mock
import sys, os

sys.path.append(os.path.abspath('./'))
from Employees import Employee
from MainTest import ResponseGenerator

FIRST_NAME = 'Wade'
LAST_NAME = 'Wilson'
FAVORTE_NUMBERS = [15, 26, 33, 60, 34]
POWERBALL = 16

first_names = iter(ResponseGenerator([' asdf ', '4Fun', 'John-Paul']))
last_names = iter(ResponseGenerator([' asdf ', 'R2D2', 'Smithers']))
favorites = iter(ResponseGenerator(['1', '1', '3', 'adfs', '5', '86', '60', '34']))
powerballs = iter(ResponseGenerator(['asdf', '34', '23']))

class EmployeesTest(unittest.TestCase):
	
	def setUp(self):
		self.emp = Employee()
		self.emp2 = Employee(FIRST_NAME, LAST_NAME, FAVORTE_NUMBERS, POWERBALL)

	def test_init(self):
		self.assertIsInstance(self.emp, Employee)
		self.assertIsInstance(self.emp2, Employee)
		print("Employee init test pass")

	def test_str(self):
		expected = 'Wade Wilson 15 26 33 60 34 Power Ball: 16'
		result = str(self.emp2)
		self.assertEqual(result, expected)
		print("Employee str test pass")

	@mock.patch('builtins.input', first_names.mock_response)
	def test_GetFirstName(self):
		self.emp.get_first_name()
		self.assertEqual(self.emp.first_name, 'John-Paul')
		print('Employee get_first_name method test pass')

	@mock.patch('builtins.input', last_names.mock_response)
	def test_GetLastName(self):
		self.emp.get_last_name()
		self.assertEqual(self.emp.last_name, 'Smithers')
		print('Employee get_last_name method test pass')

	@mock.patch('builtins.input', favorites.mock_response)
	def test_GetFavoriteNumbers(self):
		self.emp.get_favorite_numbers()
		expected = [1, 3, 5, 60, 34]
		self.assertEqual(self.emp.favorite_numbers, expected)
		print('Employee get_favorite_numbers method test pass')

	@mock.patch('builtins.input', powerballs.mock_response)
	def test_GetPowerball(self):
		self.emp.get_powerball()
		self.assertEqual(self.emp.powerball, 23)
		print('Employee get_powerball method test pass')

	def test_BuildExcludingString(self):
		#len(favorite_numbers) == 1
		self.emp.favorite_numbers = [1]
		expected = '1'
		result = self.emp.build_excluding_string()
		self.assertEqual(result, expected)

		#len(favorite_numbers) == 2
		self.emp.favorite_numbers = [1, 2]
		expected = '1 and 2'
		result = self.emp.build_excluding_string()
		self.assertEqual(result, expected)

		#len(favorite_numbers) == 3
		self.emp.favorite_numbers = [1, 2, 3]
		expected = '1, 2, and 3'
		result = self.emp.build_excluding_string()
		self.assertEqual(result, expected)

		#len(favorite_numbers) > 3
		self.emp.favorite_numbers = [1, 2, 3, 4]
		expected = '1, 2, 3, and 4'
		result = self.emp.build_excluding_string()
		self.assertEqual(result, expected)
		print('Employee build_excluding_string method test pass')

	@mock.patch('Employees.Employee.get_first_name', return_value=None)
	@mock.patch('Employees.Employee.get_last_name', return_value=None)
	@mock.patch('Employees.Employee.get_favorite_numbers', return_value=None)
	@mock.patch('Employees.Employee.get_powerball', return_value=None)
	def test_AddInfo(self, mockFirst, mockLast, mockFavorites, mockPowerball):
		self.assertIsNone(self.emp2.add_info())
		print('Employee add_info method test pass')



if __name__ == '__main__':
	unittest.main()