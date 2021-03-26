import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.clock import Clock
from math import *

class Animation(Widget):
	def __init__(self, **kwargs):
		super(Animation, self).__init__(**kwargs)
		
		#colours
		self.red = (1, 0, 0, 1)
		self.green = (0, 1, 0, 1)
		self.blue = (0, 0, 1, 1)
		self.yellow = (1, 1, 0, 1)
		self.cyan = (0, 1, 1, 1)
		self.black = (0, 0, 0, 1)
		self.white = (1, 1, 1, 1)
		self.grey = (0.5, 0.5, 0.5, 1)
		self.gray = (0.6, 0.6, 0.6, 1)
		self.brown = (0.8, 0.4, 0, 1)
		
		#background
		with self.canvas:
			Color(rgba=self.blue)
			Rectangle(size=(720, 1440))
			
			Color(rgba=self.cyan)
			Ellipse(size=(720, 1440))
			
		#player
			Color(rgba=self.gray)
			Ellipse(size=(150, 150), pos=(285, 1045))
			Color(rgba=self.red)
			Ellipse(size=(10, 10), pos=(315, 1090))
			Ellipse(size=(10, 10), pos=(395, 1090))
			
			Color(rgba=self.gray)
			Triangle(points=[235, 1045, 465, 1045, 350, 645])
			
			Color(rgba=self.grey)
			Line(points=[(350, 645), (450, 245)], width=8)
			Line(points=[(350, 645), (250, 245)], width=8)
			Line(points=[(450, 245), (470, 245)], width=8)
			Line(points=[(250, 245), (230, 245)], width=8)
			
			Line(points=[(235, 1045), (350, 745)], width=8)
			Line(points=[(465, 1045), (350, 745)], width=8)
			
		#stick
			self.speed = 0
			self.inc = 0
			self.x1, self.x2, self.y1, self.y2 = 50, 650, 745, 745
			Color(rgba=self.brown)
			self.stick = Line(points=[(self.x1, self.y1), (self.x2, self.y2)], width=5)
			
		Clock.schedule_interval(self.play, 0)
		
	def play(self, dt):
		#move
		self.x1 = 350 + (300 * sin(radians(self.speed)))
		self.y1 = 745 + (300 * cos(radians(self.speed)))
		
		self.x2 = 350 + (300 * sin(radians(self.speed-180)))
		self.y2 = 745 + (300 * cos(radians(self.speed-180)))
		
		self.speed += self.inc
		if self.speed <= 5000:
			self.inc += 0.05
		
		self.stick.points = [(self.x1, self.y1), (self.x2, self.y2)]
		
class MyApp(App):
	def build(self):
		return Animation()
		
if __name__ == "__main__":
	MyApp().run()
