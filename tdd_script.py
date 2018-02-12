import pyautogui
from time import sleep
from random import uniform, choice, randint


class RandomActions:
	def __init__(self):
		self.random_phrases = []
		with open('text') as f:
			lines = f.readlines()
			for line in lines:
				self.random_phrases.append(line.strip())
		
	def random_actions_1(self):	
		# Writing		
		phrase = choice(self.random_phrases)
		for letter in phrase:   
			pyautogui.typewrite(letter, interval=uniform(0.1, 0.3))			
		pyautogui.typewrite('\n', interval=uniform(0.3, 0.7))			
			
	def random_actions_2(self):	
		number_of_clicks = randint(1, 12)
		for click in range(number_of_clicks):
			random_x, random_y = randint(100, 1004), randint(100, 1004)
			random_duration = uniform(0.4, 0.8)
			# Moving mouse
			pyautogui.moveTo(random_x, random_y, duration=random_duration)
			# Clicking
			pyautogui.click(x=random_x, y=random_y)
			
	def random_actions_3(self):
		# Scrolling
		scroll_amount, scroll_x, scroll_y = randint(-100, 100), randint(100, 300), randint(100, 300)
		pyautogui.scroll(scroll_amount, x=scroll_x, y=scroll_y)
		
		screen_x, screen_y = pyautogui.size()
		number_of_clicks = randint(1, 12)
		for click in range(number_of_clicks):
			# Moving mouse
			random_x, random_y = randint(100, screen_x-100), randint(100, screen_y-100)
			random_duration = uniform(0.4, 0.8)
			pyautogui.moveTo(random_x, random_y, duration=random_duration)
			# Clicking			
			pyautogui.click(x=random_x, y=random_y)
			# Writing
			phrase = choice(self.random_phrases)
			for letter in phrase:   
				pyautogui.typewrite(letter, interval=uniform(0.04, 0.9))			
			pyautogui.typewrite('\n', interval=uniform(0.3, 0.7))
			
    	
if __name__ == "__main__":
	actions = RandomActions()
	functions = [actions.random_actions_1, actions.random_actions_2, actions.random_actions_3]	
	while True:
		choice(functions)()
		sleep(randint(1, 23))    	


