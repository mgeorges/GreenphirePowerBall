from PowerBall import PowerBall
from Employees import Employee

def main():
	print('\n---------------------------------------------')
	print('--- Welcome to the Employee PowerBall !!! ---')
	print('---------------------------------------------\n')
	
	powerball = PowerBall()
	not_done = True
	while not_done:
		emp = Employee()
		emp.add_info()

		powerball.add_employee(emp)
		print('\n')
		not_done = continue_adding()

	powerball.select_winning_number()
	print(powerball)

def continue_adding():
	choice = input("Add another Employee (y/n)? ")
	accepted_pos_input = ['y', 'yes']
	accepted_neg_input = ['n', 'no']

	if choice.lower() in accepted_neg_input:
		return False
	elif choice.lower() in accepted_pos_input:
		return True
	else:
		print('Sorry that is not acceptable input. Acceptable input strings include: ' + str(accepted_pos_input) + ' or ' + str(accepted_neg_input))
		print('Please try again.\n')
		return continue_adding()

if __name__ == '__main__':
	main()