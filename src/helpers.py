from OpenGL.GL import *
from OpenGL.GLU import *
import os

import pygame

class Grid:
	def __init__(self,main,y):
		self.main = main
		self.size = 50
		self.numLines = 12
		self.y = y
	def compute(self):
		pass
	def draw(self):
		glColor3f(0,0,0)
		glBegin(GL_LINES)
		for x in xrange(-self.numLines*self.size,self.numLines*self.size,self.size):
			glVertex3f(x,self.y,-self.numLines*self.size)
			glVertex3f(x,self.y,self.numLines*self.size)
		glEnd()
		glBegin(GL_LINES)
		for z in xrange(-self.numLines*self.size,self.numLines*self.size,self.size):
			glVertex3f(-self.numLines*self.size,self.y,z)
			glVertex3f(self.numLines*self.size,self.y,z)
		glEnd()

def removeCharFromString(string, removechar):
	'''Returns a string that is the original without any removechar'''
	rs = ''
	for character in string:
		if character != removechar:
			rs += character
	return rs

def getLevelText(level):
	'''Returns a string of that file. For level loading.'''
	fullname = os.path.join('data','levels',str(level) + '.py')
	in_file = open(fullname,'rU')
	text = in_file.read()
	in_file.close()
	text = removeCharFromString(text, '\r')
	return text

def loadImage(name,colorkey=None):
	fullname = os.path.join('data','images',name)
	img = pygame.image.load(fullname)
	if colorkey:
		img.set_colorkey(colorkey)
	return img, img.get_rect()
