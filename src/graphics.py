from OpenGL.GL import *
from OpenGL.GLU import *
import math
import random

class Dots:
	def __init__(self,main):
		self.main = main

		self.points = []
		'''numPoints = 2400
		rad = 1200
		for x in xrange(0,numPoints):
			thisRad = random.random()**.5*rad #Try to be more commonly on the outside
			a1 = random.random()*math.pi*2
			a2 = random.random()*math.pi*2
			x = thisRad*math.cos(a2)
			y = thisRad*math.sin(a1)*math.sin(a2)
			z = thisRad*math.cos(a1)*math.sin(a2)
			self.points.append([x,y,z])'''
		rad = 1600
		angChange = math.pi/24
		a1 = 0
		while a1 < math.pi*2:
			a2 = 0
			while a2 < math.pi*2:
				x = rad*math.sin(a1)*math.sin(a2)
				y = rad*math.cos(a2)
				z = rad*math.cos(a1)*math.sin(a2)
				self.points.append([x,y,z])
				a2 += angChange
			a1 += angChange
	def compute(self):
		pass
	def draw(self):
		glBegin(GL_POINTS)
		glColor3f(1,1,1)
		for point in self.points:
			glVertex3f(point[0],point[1],point[2])
		glEnd()
