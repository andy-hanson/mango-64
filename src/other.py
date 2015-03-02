from OpenGL.GL import *
from OpenGL.GLU import *
import math

import mango
import plat

class LazyCamera:
	def __init__(self,main):
		self.main = main
		for anObject in self.main.objects:
			if isinstance(anObject,mango.Mango):
				self.mango = anObject
		self.yPlus = -40
		self.trackMangoY = 0
	def compute(self):
		self.main.camY = self.yPlus + self.main.xzRad * math.sin(self.main.camRotX*math.pi/128) + self.trackMangoY

		diff = abs(self.trackMangoY - self.mango.y)
		speed = diff**4/33554432
		if self.trackMangoY < self.mango.y:
			self.trackMangoY += speed
			if self.trackMangoY > self.mango.y:
				self.trackMangoY = self.mango.y
		if self.trackMangoY > self.mango.y:
			self.trackMangoY -= speed
			if self.trackMangoY < self.mango.y:
				self.trackMangyY = self.mango.y
	def draw(self):
		pass

class PlatXMover:
	def __init__(self,main,color,x1,x2,y,z,sinSpeed=.01,size=30,):
		self.main = main
		self.x1 = x1
		self.x2 = x2
		self.y = y
		self.z = z
		self.sinSpeed = sinSpeed
		self.sinX = 0
		self.plat = plat.Plat(self.main,color,x1,z,size,y)
		self.main.objects.append(self.plat)
	def compute(self):
		self.sinX += self.sinSpeed
		self.plat.setPos((self.x1 + self.x2)/2 + (self.x2 - self.x1)/2*math.sin(self.sinX),self.y,self.z)
	def draw(self):
		pass

class PlatYMover:
	def __init__(self,main,color,x,y1,y2,z,sinSpeed=.01,size=30):
		self.main = main
		self.x = x
		self.y1 = y1
		self.y2 = y2
		self.z = z
		self.sinSpeed = sinSpeed
		self.sinX = 0
		self.plat = plat.Plat(self.main,color,x,z,size,y1)
		self.main.objects.append(self.plat)
	def compute(self):
		self.sinX += self.sinSpeed
		self.plat.setPos(self.x,(self.y1 + self.y2)/2 + (self.y2 - self.y1)/2*math.sin(self.sinX),self.z)
	def draw(self):
		pass

class PlatZMover:
	def __init__(self,main,color,x,y,z1,z2,sinSpeed=.01,size=30):
		self.main = main
		self.x = x
		self.y = y
		self.z1 = z1
		self.z2 = z2
		self.sinSpeed = sinSpeed
		self.sinX = 0
		self.plat = plat.Plat(self.main,color,x,z1,size,y)
		self.plat.color = color
		self.main.objects.append(self.plat)
	def compute(self):
		self.sinX += self.sinSpeed
		self.plat.setPos(self.x,self.y,(self.z1 + self.z2)/2 + (self.z2 - self.z1)/2*math.sin(self.sinX))
	def draw(self):
		pass

class PlatCircle:
	def __init__(self,main,color,numPlats,y,minRad,maxRad,sinSpeed,angleSpeed,size=30,minY=None,maxY=None,ySinSpeed=None):
		self.main = main
		self.numPlats = numPlats
		self.y = y
		self.minRad = minRad
		self.maxRad = maxRad
		self.sinSpeed = sinSpeed
		self.angleSpeed = angleSpeed

		self.plats = []
		for x in xrange(0,self.numPlats):
			new = plat.Plat(self.main,color,0,size,0,size,0)
			self.plats.append(new)
			self.main.objects.append(new)

		self.angle = 0
		self.sinX = 0


		self.minY = minY
		self.maxY = maxY
		self.ySinX = 0
		self.ySinSpeed = ySinSpeed

	def compute(self):
		self.sinX += self.sinSpeed
		rad = (self.maxRad + self.minRad)/2 + (self.maxRad - self.minRad)/2*math.sin(self.sinX)

		if self.minY:
			self.ySinX += self.ySinSpeed
			self.y = (self.maxY + self.minY)/2 + (self.maxY - self.minY)/2*math.sin(self.ySinX)

		self.angle += self.angleSpeed
		thisAngle = self.angle
		for plat in self.plats:
			x = rad*math.cos(thisAngle)
			y = self.y
			z = rad*math.sin(thisAngle)
			plat.setPos(x,y,z)
			thisAngle += 2*math.pi/self.numPlats

	def draw(self):
		pass


class Goal:
	def __init__(self,main,x,y,z):
		self.main = main
		self.x = x
		self.y = y
		self.z = z
		self.size = 25
	def compute(self):
		for anObject in self.main.objects:
			if isinstance(anObject,mango.Mango):
				if self.x - self.size < anObject.x < self.x + self.size and \
				   self.y - self.size < anObject.y < self.y + self.size and \
				   self.z - self.size < anObject.z < self.z + self.size:
					self.main.win()
	def draw(self):
		glPushMatrix()

		glTranslatef(self.x,self.y,self.z)

		glColor3f(1,1,.75)
		glBegin(GL_QUADS) #Directions are looking at it

		#Back
		glVertex3f(-self.size,-self.size,-self.size)
		glVertex3f(-self.size,self.size,-self.size)
		glVertex3f(self.size,self.size,-self.size)
		glVertex3f(self.size,-self.size,-self.size)

		#Front
		glVertex3f(-self.size,-self.size,self.size)
		glVertex3f(self.size,-self.size,self.size)
		glVertex3f(self.size,self.size,self.size)
		glVertex3f(-self.size,self.size,self.size)

		#Left side
		glVertex3f(-self.size,self.size,-self.size)
		glVertex3f(-self.size,-self.size,-self.size)
		glVertex3f(-self.size,-self.size,self.size)
		glVertex3f(-self.size,self.size,self.size)

		#Right side
		glVertex3f(self.size,self.size,self.size)
		glVertex3f(self.size,-self.size,self.size)
		glVertex3f(self.size,-self.size,-self.size)
		glVertex3f(self.size,self.size,-self.size)

		#Top
		glVertex3f(-self.size,self.size,-self.size)
		glVertex3f(-self.size,self.size,self.size)
		glVertex3f(self.size,self.size,self.size)
		glVertex3f(self.size,self.size,-self.size)

		#Bottom
		glVertex3f(self.size,self.size,-self.size)
		glVertex3f(self.size,self.size,self.size)
		glVertex3f(-self.size,self.size,self.size)
		glVertex3f(-self.size,self.size,-self.size)

		glEnd()

		glPopMatrix()

