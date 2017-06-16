import unittest
from unittest import mock
import sys, os

sys.path.append(os.path.abspath('./'))
from MainTest import ResponseGenerator
from PowerBall import PowerBall
from Employees import Employee

EMPLOYEES_LIST = [
	Employee('A', 'A', [1, 2, 3, 4, 5], 23),
	Employee('B', 'B', [1, 2, 3, 5, 4], 23),
	Employee('C', 'C', [1, 2, 3, 4, 69], 23),
	Employee('D', 'D', [1, 2, 3, 40, 50], 12),
	Employee('E', 'E', [1, 2, 30, 23, 33], 12),
	Employee('F', 'F', [1, 22, 21, 20, 31], 15)
]

random_num = iter(ResponseGenerator([1, 2, 3, 4, 5]))

class PowerBallTest(unittest.TestCase):

	def setUp(self):
		self.powerball = PowerBall()
		self.emp1 = Employee('Wade', 'Wilson', [1, 2, 3, 4, 5], 23)
		self.emp2 = Employee('Frank', 'Castle', [1, 62, 33, 24, 15], 22)
		self.emp3 = Employee('Austin', 'Powers', [1, 2, 3, 4, 5], 23)

	def test_init(self):
		self.assertIsInstance(self.powerball, PowerBall)
		print('PowerBall init test pass')

	def test_str(self):
		self.powerball.add_employee(self.emp3)
		self.powerball.winning_powerball = self.emp3.powerball
		self.powerball.winning_numbers = self.emp3.favorite_numbers
		self.powerball.find_winner()

		expected = '\n' + str(self.emp3) + '\n\n\nPowerball winning number:\n\n1 2 3 4 5 Powerball: 23\n\nWE HAVE A WINNER: Austin Powers'
		result = str(self.powerball)
		self.assertEqual(result, expected)
		print('PowerBall string test pass')

	def test_AddEmployee(self):
		self.powerball.add_employee(self.emp1)
		self.assertEqual(len(self.powerball.employees), 1)
		self.assertEqual(self.powerball.favorites_duplicate_count[1], 1)
		self.assertEqual(self.powerball.powerball_duplicate_count[23], 1)
		print('PowerBall add_employee method test pass')

	@mock.patch('PowerBall.PowerBall.choose_winning_powerball', return_value=None)
	@mock.patch('PowerBall.PowerBall.choose_winning_numbers', return_value=None)
	@mock.patch('PowerBall.PowerBall.find_winner', return_value=None)
	def test_SelectWinningNumber(self, mockPowerball, mockNumbers, mockWinner):
		self.assertIsNone(self.powerball.select_winning_number())
		print('PowerBall select_winning_number method test pass')

	def test_AddDuplicateCounts(self):
		self.powerball.add_duplicate_counts(self.emp2)
		self.powerball.add_duplicate_counts(self.emp1)
		self.assertEqual(len(self.powerball.favorites_duplicate_count), 9)
		self.assertEqual(self.powerball.favorites_duplicate_count[1], 2)
		print('PowerBall add_duplicate_counts method test pass')

	@mock.patch('random.choice', return_value=22)
	def test_ChooseWinningPowerball(self, mockRandom):
		self.powerball.add_employee(self.emp1)
		self.powerball.choose_winning_powerball()
		self.assertEqual(self.powerball.winning_powerball, 23)

		self.powerball.add_employee(self.emp2)
		self.powerball.choose_winning_powerball()
		self.assertEqual(self.powerball.winning_powerball, 22)
		print('PowerBall choose_winning_powerball method test pass')
		
	def test_ChooseWinningNumbers(self):
		for employee in EMPLOYEES_LIST:
			self.powerball.add_employee(employee)
		self.powerball.choose_winning_numbers()
		self.assertEqual(self.powerball.winning_numbers, [1, 2, 3, 4, 5])
		print('PowerBall choose_winning_numbers method test pass')

	@mock.patch('random.choice', random_num.mock_response)
	def test_ChooseWinningNumbers_random(self):
		self.powerball.add_employee(self.emp1)
		self.powerball.choose_winning_numbers()
		self.assertEqual(self.powerball.winning_numbers, [1, 2, 3, 4, 5])
		print('PowerBall choose_winning_numbers random method test pass')

	def test_FindWinner(self):
		self.powerball.add_employee(self.emp2)
		self.powerball.add_employee(self.emp1)
		self.powerball.winning_numbers = self.emp1.favorite_numbers
		self.powerball.winning_powerball = self.emp1.powerball
		self.powerball.find_winner()
		self.assertEqual(self.powerball.winner, 'Wade Wilson')

		self.powerball.winner = None
		self.powerball.add_employee(self.emp3)
		self.powerball.find_winner()
		self.assertEqual(self.powerball.winner, 'Wade Wilson, Austin Powers')
		print('PowerBall find_winner method test pass')



if __name__ == '__main__':
	unittest.main()