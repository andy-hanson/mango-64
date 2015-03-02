self.objects.append(mango.Mango(self,300,120,300))
self.objects.append(other.LazyCamera(self))

self.objects.append(plat.Plat(self,(0,.75,1),-800,800,-800,800,-1))

sinSpeed = 0.03125
size = 60
self.objects.append(other.PlatYMover(self,(.5,.5,.5),300,40,120,300,sinSpeed,size))
self.objects.append(other.PlatYMover(self,(1,1,1),300,240,360,300,sinSpeed,size))
self.objects.append(other.PlatYMover(self,(.5,.5,.5),300,280,420,-300,sinSpeed,size))
self.objects.append(plat.Plat(self,(1,1,1),300,-300,size,640))

numPlats = 8
sinSpeed = 0.005859375 #For radius
angleSpeed = 0.00390625
minY = 680
maxY = 760
ySinSpeed = 0.0078125
size = 120
self.objects.append(other.PlatCircle(self,(0,0,1),numPlats,None,math.sqrt(300**2*2)*3/4,math.sqrt(300**2*2)*4/4,sinSpeed,angleSpeed,size,minY,maxY,ySinSpeed))

numPlats = 4
minY = 740
maxY = 820
angleSpeed = 0.005859375
sinSpeed = 0.005859375
ySinSpeed = 0.015625
self.objects.append(other.PlatCircle(self,(0,1,0),numPlats,None,math.sqrt(300**2*2)*2/4,math.sqrt(300**2*2)*3/4,sinSpeed,angleSpeed,size,minY,maxY,ySinSpeed))

minY = 800
maxY = 880
sinSpeed = 0.005859375
angleSpeed = 0.00390625
ySinSpeed = 0.0078125
self.objects.append(other.PlatCircle(self,(1,0,0),numPlats,None,math.sqrt(300**2*2)*1/4,math.sqrt(300**2*2)*2/4,sinSpeed,angleSpeed,size,minY,maxY,ySinSpeed))

self.objects.append(other.Goal(self,0,920,0))

