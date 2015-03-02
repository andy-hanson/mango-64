from OpenGL.GL import *
from OpenGL.GLU import *
import math

import plat

class Mango:
	def __init__(self,main,x,y,z):
		self.main = main
		self.x = x
		self.y = y
		self.z = z

		self.size = 5

		self.xzdir = math.pi #Start facing that way because I said so.
		self.xzdirvel = 0
		self.xzdirspeed = 0.03125

		self.yVel = 0
		self.normalGrav = .075
		self.AGrav = .0215
		self.grav = self.normalGrav
		self.hop = 1.66
		self.onGround = True

		self.moveVel = 0
		self.moveVelChange = 0
		self.groundAccelSpeed = .02
		self.turnResistance = .975
		self.normalResistance = .997
		self.resistance = self.normalResistance

		self.platform = None
		self.platformX = None
		self.platformY = None
		self.platformZ = None
		self.platformXVel = 0
		self.platformYVel = 0
		self.platformZVel = 0

	def compute(self):
		self.yVel -= self.grav
		self.y += self.yVel
		if self.y < -800:
			self.main.lose()
		hasCollide = 0
		for anObject in self.main.objects:
			if isinstance(anObject,plat.Plat):
				if anObject.checkCollide(self):
					self.onGround = 1
					self.yVel = 0
					self.y = anObject.y + self.size
					hasCollide = 1
					if anObject is not self.platform:
						self.platform = anObject
						self.platformX = anObject.centerX
						self.platformY = anObject.y
						self.platformZ = anObject.centerZ
		if not hasCollide:
			self.onGround = 0
			self.platform = None


		self.moveVel += self.moveVelChange
		self.moveVel *= self.resistance
		if self.moveVel < 0:
			self.moveVel = 0

		self.xzdir += self.xzdirvel
		self.x += self.moveVel*math.sin(self.xzdir)
		self.z += self.moveVel*math.cos(self.xzdir)

		if self.platform:
			self.x += self.platform.centerX - self.platformX
			if 1:#self.platform.y - self.platformY > 0: #You don't get pulled down #YES YOU DO!
				self.y += self.platform.y - self.platformY
			self.z += self.platform.centerZ - self.platformZ
			self.platformXVel = self.platform.centerX - self.platformX
			self.platformYVel = self.platform.y - self.platformY
			self.platformZVel = self.platform.centerZ - self.platformZ
			self.platformX = self.platform.centerX
			self.platformY = self.platform.y
			self.platformZ = self.platform.centerZ

		self.main.yRot = math.atan2(self.x,self.z)
	def draw(self):
		glPushMatrix()

		glTranslatef(self.x,self.y,self.z)
		glRotatef(self.xzdir*180/math.pi,0,1,0)

		glColor3f(1,.5,0)
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

		#SHADOWS
		glPushMatrix()

		#Find the platform to draw the shadow to.
		shadowPlat = None
		y = None
		for anObject in self.main.objects:
			if isinstance(anObject,plat.Plat):
				if anObject.x1 < self.x < anObject.x2 and anObject.z1 <self.z < anObject.z2 and self.y > anObject.y:
					if y:
						if anObject.y > y:
							shadowPlat = anObject
							y = anObject.y
						else:
							pass #There's a plat above it
					else:
						shadowPlat = anObject
						y = anObject.y

		glBegin(GL_QUADS)
		glColor3f(0,0,0)
		size2 = self.size*math.sqrt(2)

		if shadowPlat:
			yPlus = .1 #So depth is different
			for k in xrange(0,4):
				ang = -self.xzdir + math.pi*2*k/4 - math.pi/4
				x = size2*math.cos(ang) + self.x
				z = size2*math.sin(ang) + self.z
				glVertex3f(x,shadowPlat.y+yPlus,z)
		glEnd()
		glPopMatrix()
	def leftKeyDown(self):
		self.xzdirvel = self.xzdirspeed
	def rightKeyDown(self):
		self.xzdirvel = -self.xzdirspeed
	def upKeyDown(self):
		if self.onGround:
			self.moveVelChange = self.groundAccelSpeed
		else:
			self.moveVelChange = self.groundAccelSpeed

	def downKeyDown(self):
		self.resistance = self.turnResistance
	def leftKeyUp(self):
		self.xzdirvel = 0
	def rightKeyUp(self):
		self.xzdirvel = 0
	def upKeyUp(self):
		self.moveVelChange = 0
	def downKeyUp(self):
		self.resistance = self.normalResistance
	def spaceKeyDown(self):
		if self.onGround:
			if self.platformYVel > 0:
				self.yVel = self.hop + self.platformYVel
			else:
				self.yVel = self.hop
			xVel = self.moveVel * math.sin(self.xzdir)
			zVel = self.moveVel * math.cos(self.xzdir)
			xVel += self.platformXVel
			zVel += self.platformZVel
			self.moveVel = math.sqrt(xVel**2 + zVel**2)
			self.xzdir = math.atan2(xVel,zVel)
			self.onGround = 0
		self.grav = self.AGrav
	def spaceKeyUp(self):
		self.grav = self.normalGrav
