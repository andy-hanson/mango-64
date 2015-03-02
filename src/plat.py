from OpenGL.GL import *
from OpenGL.GLU import *

import helpers

class Plat:
	def __init__(self,main,color,a1,a2,a3,a4,a5=None):
		self.main = main
		if a5 is not None:
			self.x1 = a1
			self.x2 = a2
			self.z1 = a3
			self.z2 = a4
			self.y =  a5
		else:
			self.x1 = a1 - a3
			self.x2 = a1 + a3
			self.z1 = a2 - a3
			self.z2 = a2 + a3
			self.y = a4
		self.color = color
	def compute(self):
		#For computations:
		self.centerX = (self.x1 + self.x2)/2
		self.centerZ = (self.z1 + self.z2)/2
	def draw(self):
		glColor3fv(self.color)
		glBegin(GL_QUADS)
		glVertex3f(self.x1,self.y,self.z1)
		glVertex3f(self.x1,self.y,self.z2)
		glVertex3f(self.x2,self.y,self.z2)
		glVertex3f(self.x2,self.y,self.z1)
		glEnd()

		if self.y > 0:
			#Draw a shadow
			glColor3f(0,0,0)
			glBegin(GL_QUADS)
			glVertex3f(self.x1,0,self.z1)
			glVertex3f(self.x1,0,self.z2)
			glVertex3f(self.x2,0,self.z2)
			glVertex3f(self.x2,0,self.z1)
			glEnd()

			for anObject in self.main.objects:
				if isinstance(anObject,helpers.Grid) and self.y > anObject.y:
					glColor3f(0,0,0)
					glBegin(GL_QUADS)
					glVertex3f(self.x1,anObject.y,self.z1)
					glVertex3f(self.x1,anObject.y,self.z2)
					glVertex3f(self.x2,anObject.y,self.z2)
					glVertex3f(self.x2,anObject.y,self.z1)
					glEnd()


	def checkCollide(self,mango):
		if self.x1 < mango.x < self.x2 and self.z1 < mango.z < self.z2:
			if mango.yVel < 0:
				#It's moving down.
				if self.y - mango.size*2 < mango.y - mango.size < self.y:
					return 1
			if mango.yVel > 0:
				#It's moving up.
				return 0


	def setPos(self,x,y,z):
		self.centerX = x
		self.centerZ = z
		xSize = (self.x2 - self.x1)/2
		zSize = (self.z2 - self.z1)/2
		self.x1 = x - xSize
		self.x2 = x + xSize
		self.z1 = z - zSize
		self.z2 = z + zSize
		self.y = y
