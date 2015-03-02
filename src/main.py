import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

import math
import random

import graphics
import helpers
import mango
import other
import plat

import EZMenu

class Main:
	def __init__(self):
		fontSize = 72
		level = int(EZMenu.EZMenu('Choose a level! :D',['Level 1','Level 2','Level 3'],fontSize)[6]) - 1 #Pretend levels are numbered 1-3 but they're really 0-2

		self.FPS = 80

		# Turned off because if there are bugs there's no escape!
		#fullscreen =  EZMenu.EZMenu('Fullscreen?',['Yes Yes','No No No'],fontSize)
		self.fullscreen = False # fullscreen == 'Yes Yes'

		self.w = 800
		self.h = 800
		pygame.init()
		if self.fullscreen:
			s = pygame.display.set_mode((0,0),pygame.OPENGL|pygame.FULLSCREEN|pygame.HWSURFACE)
			self.w = s.get_width()
			self.h = s.get_height()
		else:
			s = pygame.display.set_mode((self.w,self.h),pygame.OPENGL)

		glViewport(0, 0, self.w, self.h)
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		gluPerspective(45,float(self.w)/self.h,1.0,3200.0)
		glClearColor(0,0,.25,0)

		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)
		glEnable(GL_POINT_SMOOTH)
		glPointSize(4)

		glClearDepth(1.0)
		glEnable(GL_DEPTH_TEST)

		self.objects = []

		exec(helpers.getLevelText(level))



		self.yRot = 0 #Rotation about y axis. Camera always looks at x=0,z=0
		self.xzRad = 1200
		self.camX = 0
		self.camY = 0
		self.camZ = 0
		self.minCamRotX = 5
		self.maxCamRotX = 45
		self.camRotX = 17.5
		self.camRotXChange = 0
		self.camRotXChangeSpeed = 0.125

		self.clock = pygame.time.Clock()

	def compute(self):
		for anObject in self.objects:
			anObject.compute()

	def draw(self):
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

		glPushMatrix()

		self.camRotX += self.camRotXChange
		if self.camRotX < self.minCamRotX:
			self.camRotX = self.minCamRotX
		if self.camRotX > self.maxCamRotX:
			self.camRotX = self.maxCamRotX
		glRotatef(self.camRotX,1,0,0)
		glRotatef(-self.yRot*180/math.pi,0,1,0)
		self.camX = self.xzRad*math.sin(self.yRot)
		self.camZ = self.xzRad*math.cos(self.yRot)
		glTranslatef(-self.camX,-self.camY,-self.camZ)

		for anObject in self.objects:
			anObject.draw()

		glPopMatrix()

		glFlush()

	def go(self):
		self.done = 0
		while not self.done:
			self.compute()
			self.draw()
			pygame.display.flip()
			self.getEvents()
			self.clock.tick(self.FPS)
			pygame.display.set_caption('Mango 64 Jul 24 09 - framerate ' + str(self.clock.get_fps()) + '/' + str(self.FPS))

		pygame.quit()

	def getEvents(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.done = 1
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					for anObject in self.objects:
						try:
							anObject.upKeyDown()
						except AttributeError:
							pass
				if event.key == pygame.K_LEFT:
					for anObject in self.objects:
						try:
							anObject.leftKeyDown()
						except AttributeError:
							pass
				if event.key == pygame.K_RIGHT:
					for anObject in self.objects:
						try:
							anObject.rightKeyDown()
						except AttributeError:
							pass
				if event.key == pygame.K_DOWN:
					for anObject in self.objects:
						try:
							anObject.downKeyDown()
						except AttributeError:
							pass
				if event.key == pygame.K_SPACE:
					for anObject in self.objects:
						try:
							anObject.spaceKeyDown()
						except AttributeError:
							pass
				if event.key == pygame.K_a:
					self.camRotXChange = self.camRotXChangeSpeed
				if event.key == pygame.K_z:
					self.camRotXChange = -self.camRotXChangeSpeed
				if event.key == pygame.K_ESCAPE:
					self.done = 1
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					for anObject in self.objects:
						try:
							anObject.upKeyUp()
						except AttributeError:
							pass
				if event.key == pygame.K_DOWN:
					for anObject in self.objects:
						try:
							anObject.downKeyUp()
						except AttributeError:
							pass
				if event.key == pygame.K_LEFT:
					for anObject in self.objects:
						try:
							anObject.leftKeyUp()
						except AttributeError:
							pass
				if event.key == pygame.K_RIGHT:
					for anObject in self.objects:
						try:
							anObject.rightKeyUp()
						except AttributeError:
							pass
				if event.key == pygame.K_SPACE:
					for anObject in self.objects:
						try:
							anObject.spaceKeyUp()
						except AttributeError:
							pass
				if event.key == pygame.K_a:
					self.camRotXChange = 0
				if event.key == pygame.K_z:
					self.camRotXChange = 0

	def win(self):
		print 'win'
		self.done = 1
	def lose(self):
		print 'lose'
		self.done = 1


k = Main()
k.go()
