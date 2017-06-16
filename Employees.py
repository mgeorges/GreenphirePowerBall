import re

class Employee:

    def __init__(self, first_name='', last_name='', favorite_numbers=[], powerball=None):
        self.first_name = first_name
        self.last_name = last_name
        self.favorite_numbers = favorite_numbers
        self.powerball = powerball

    def __str__(self):
    	output = self.first_name + " " + self.last_name
    	for num in self.favorite_numbers:
    		output += " " + str(num)
    	output += " Power Ball: " + str(self.powerball)
    	return output

    def get_first_name(self):
    	first_name = input("Enter your first name: ")
    	if re.match("^[A-Za-z\-]*$", first_name):
    		self.first_name = first_name
    	else:
    		print("That doesn't look right. Try again.")
    		self.get_first_name()

    def get_last_name(self):
    	last_name = input("Enter your last name: ")
    	if re.match("^[A-Za-z\-]*$", last_name):
    		self.last_name = last_name
    	else:
    		print("That doesn't look right. Try again")
    		self.get_last_name()

    def get_favorite_numbers(self):
    	current_favorite_num = 1
    	while current_favorite_num <= 5:
    		if current_favorite_num == 1:
    			num = input("select 1st # (1 thru 69): ")
    		elif current_favorite_num == 2:
    			num = input("select 2nd # (1 thru 69 excluding %s): " % self.build_excluding_string())
    		elif current_favorite_num == 3:
    			num = input("select 3rd # (1 thru 69 excluding %s): " % self.build_excluding_string())
    		else: 
    			num = input("select %dth # (1 thru 69 excluding %s): " % (current_favorite_num, self.build_excluding_string()))

    		if num.isdigit():
    			int_num = int(num)
    			if (int_num not in self.favorite_numbers) and (1 <= int_num <= 69):
    				self.favorite_numbers.append(int_num)
    				current_favorite_num += 1
    			else:
    				print("You did not enter a valid number. Try again.")
    		else:
    			print("You need to enter an integer. Try again.")

    def get_powerball(self):
    	powerball = input("select Power Ball # (1 thru 26): ")
    	if powerball.isdigit() and (1 <= int(powerball) <= 26):
    		self.powerball = int(powerball)
    	else:
    		print("You need to enter an integer between 1 and 26. Try again.")
    		self.get_powerball()

    def build_excluding_string(self):
    	num_faves = len(self.favorite_numbers)
    	if (num_faves == 1):
    		return str(self.favorite_numbers[0])
    	elif (num_faves == 2):
    		return str(self.favorite_numbers[0]) + " and " + str(self.favorite_numbers[1])
    	elif (num_faves == 3):
    		return str(self.favorite_numbers[0]) + ", " + str(self.favorite_numbers[1]) + ", and " + str(self.favorite_numbers[2])
    	else:
    		return str(self.favorite_numbers[0]) + ", " + str(self.favorite_numbers[1]) + ", " + str(self.favorite_numbers[2]) + ", and " + str(self.favorite_numbers[3])
    
    def add_info(self):
        self.get_first_name()
        self.get_last_name()
        self.get_favorite_numbers()
        self.get_powerball()