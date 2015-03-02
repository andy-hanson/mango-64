self.objects.append(mango.Mango(self,0,50,500))
self.objects.append(plat.Plat(self,(0,.75,1),-600,600,-600,600,-1))

rad = 300
angChange = math.pi/12
yChange = 25
num = 24
size = 40
for x in xrange(0,num):
    ang = math.pi/2 + x*angChange
    y = (num/2 - abs(x - num/2))*yChange + .1
    if x % 2:
        color = (1,0,.5)
    else:
        color = (0,1,.5)
    self.objects.append(plat.Plat(self,color,rad*math.cos(ang),rad*math.sin(ang),size,y))

color = (.82,.64,.13)
size = 60
self.objects.append(other.PlatZMover(self,color,0,yChange*num/2 + yChange*1,-200,200,0.01,size))

self.objects.append(plat.Plat(self,(1,1,1),0,300,40,yChange*num/2+60))

numPlats = 6
y = yChange*num/2 + 120
minRad = 300
maxRad = 300
sinSpeed = 0 #No rad change
angleSpeed = 0.015625
size = 120
color = (.5,1,.25)
self.objects.append(other.PlatCircle(self,color,numPlats,y,minRad,maxRad,sinSpeed,angleSpeed,size))

self.objects.append(other.Goal(self,0,yChange*num/2 + 180,-280))

self.objects.append(other.LazyCamera(self))
