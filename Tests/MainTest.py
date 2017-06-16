import unittest
from unittest import mock
import sys, os

sys.path.append(os.path.abspath('./'))
from main import main, continue_adding


class ResponseGenerator:

	def __init__(self, responses):
		self.responses = responses
		self.index = 0

	def __next__(self):
		ret_val = self.responses[self.index]
		self.index += 1
		return ret_val

	def __iter__(self):
		return self

	def mock_response(self, prompt):
		return next(self)

mock_continue = iter(ResponseGenerator(['yessir', 'ok', 'yes']))
mock_discontinue = iter(ResponseGenerator(['nay', 'I dont think so', 'no']))
mock_main = iter(ResponseGenerator(['Austin', 'Powers', '1', '2', '3', '4', '5', '6', 'no']))

class MainTest(unittest.TestCase):

	@mock.patch('builtins.input', mock_main.mock_response)
	def test_main(self):
		self.assertIsNone(main())
		print("Main test pass")

	@mock.patch('builtins.input', mock_continue.mock_response)
	def test_ContinueAdding_true(self):
		self.assertTrue(continue_adding())
		print('continue_adding - return true - function test pass')

	@mock.patch('builtins.input', mock_discontinue.mock_response)
	def test_ContinueAdding_false(self):
		self.assertFalse(continue_adding())
		print('continue_adding - return false - function test pass')




if __name__ == '__main__':
	unittest.main()