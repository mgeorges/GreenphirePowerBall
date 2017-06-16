from Employees import Employee
import random

class PowerBall:

	def __init__(self):
		self.employees = []
		self.favorites_duplicate_count = {}
		self.powerball_duplicate_count = {}
		self.winning_numbers = []
		self.winning_powerball = 0
		self.winner = None

	def __str__(self):
		output = '\n'
		for emp in self.employees:
			output += str(emp) + '\n'
		output += '\n\nPowerball winning number:\n\n'
		for num in self.winning_numbers:
			output += str(num) + ' '
		output += 'Powerball: ' + str(self.winning_powerball)
		if self.winner:
			output+= '\n\nWE HAVE A WINNER: ' + self.winner
		return output

	def add_employee(self, emp):		
		#add employee to list of employees and update duplicate counts
		self.employees.append(emp)
		self.add_duplicate_counts(emp)

	def select_winning_number(self):
		self.choose_winning_powerball()
		self.choose_winning_numbers()
		self.find_winner()

	def add_duplicate_counts(self, emp):
		#add selected favorite numbers to duplicates count
		for num in emp.favorite_numbers:
			if num in self.favorites_duplicate_count:
				self.favorites_duplicate_count[num] += 1
			else:
				self.favorites_duplicate_count[num] = 1
		
		#add selected powerball to duplicates count
		if emp.powerball in self.powerball_duplicate_count:
			self.powerball_duplicate_count[emp.powerball] += 1
		else:
			self.powerball_duplicate_count[emp.powerball] = 1

	def choose_winning_powerball(self):
		highest_count = max(self.powerball_duplicate_count.values())
		powerball_choices = []
		for num, count in self.powerball_duplicate_count.items():
			if count == highest_count:
				powerball_choices.append(num)
		
		if len(powerball_choices) > 1:
			self.winning_powerball = random.choice(powerball_choices)
		else:
			self.winning_powerball = powerball_choices[0]

	def choose_winning_numbers(self):
		counts = set(self.favorites_duplicate_count.values())
		while (len(self.winning_numbers) < 5):
			highest_count = max(counts)
			counts.remove(highest_count)
			count_choices = []

			#find the numbers with the highest duplicate counts
			for num, count in self.favorites_duplicate_count.items():
				if count == highest_count:
					count_choices.append(num)

			#add the numbers with the highest duplicate counts to the list of the winning numbers
			while (len(self.winning_numbers) < 5 and len(count_choices) > 0):
				if len(count_choices) == 1:
					num_selected = count_choices[0]
				else:
					num_selected = random.choice(count_choices)
				self.winning_numbers.append(num_selected)
				count_choices.remove(num_selected)

	def find_winner(self):
		for emp in self.employees:
			if (emp.favorite_numbers == self.winning_numbers) and (emp.powerball == self.winning_powerball):
				if self.winner:
					self.winner += ', ' + emp.first_name + ' ' + emp.last_name
				else:
					self.winner = emp.first_name + ' ' + emp.last_name




		