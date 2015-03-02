self.objects.append(mango.Mango(self,0,120,600))
self.objects.append(other.LazyCamera(self))

self.objects.append(plat.Plat(self,(0,.75,1),-800,800,-800,800,-1))

start = 600
size = 50
dist = 200

self.objects.append(plat.Plat(self,(1,1,1),0,   start,          size,80))
self.objects.append(plat.Plat(self,(1,1,1),0,   start-dist,     size,40))
self.objects.append(plat.Plat(self,(0,0,1),0,   start-dist,     size,80))
self.objects.append(plat.Plat(self,(0,1,0),dist,start-dist,     size,80))
self.objects.append(plat.Plat(self,(1,0,0),dist,start-2*dist,   size,80))

sinSpeed = 0.015625
angleSpeed = 0.00390625
minRad = 100
maxRad = 150
size = 100
self.objects.append(other.PlatCircle(self,(.5,.5,.5),3,80,minRad,maxRad,.01,.01,size))

size = 50
self.objects.append(plat.Plat(self,(1,0,0),-dist,   -dist,  size,80))
self.objects.append(plat.Plat(self,(0,1,0),-dist,   -2*dist,size,80))
self.objects.append(plat.Plat(self,(0,0,.5),0,      -2*dist,size,80))
sinSpeed = 0.015625
self.objects.append(other.PlatYMover(self,(.25,.75,.5),0,120,380,-2*dist,sinSpeed,size))

self.objects.append(plat.Plat(self,(.82,.64,.13),0,-2*dist,size,560))

sinSpeed = 0.015625
angleSpeed = 0.00390625
minRad = 100
maxRad = 150
size = 100
self.objects.append(other.PlatCircle(self,(.5,1,.25),3,440,minRad,maxRad,.01,.01,size))
self.objects.append(other.Goal(self,0,480,0))

#self.objects.append(graphics.Dots(self))
