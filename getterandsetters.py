


class Animals:
    def __init__(self, reproduction, canmove):
        self.reproduction = reproduction
        self.canmove = canmove

def getReproduction(self):
    return self.reproduction
def getCanmove(self):
    return self.canmove


class Mammals(Animals):
    def __init__(self, reproduction, canmove, bloodtype, skin):
        super().__init__(reproduction, canmove)
        self.bloodtype = bloodtype
        self.skin = skin
def getBloodtype(self):
    return self.bloodtype
def getSkin(self):
    return self.skin            
    
           

mammalOne = Mammals("birth", "walking", "warmblooded", "hair")
print(mammalOne.reproduction)
print(mammalOne.canmove)
print(mammalOne.skin)



class Reptiles(Animals):
    def __init__(self,reproduction, canmove, bloodtype, skin):
        super().__init__(reproduction, canmove)
        self.bloodtype = bloodtype
        self.skin = skin
def getBloodtype(self):
    return self.bloodtype
def getSkin(self):
    return self.skin            

    

reptileOne = Reptiles("layeggs", "swimming", "coldblooded", "scales")
print(reptileOne.canmove)
print(reptileOne.reproduction)
print(reptileOne.skin)


class Birds(Animals):
    def __init__(self, reproduction, canmove, bloodtype, skin):
        super().__init__(reproduction, canmove)
        self.bloodtype = bloodtype
        self.skin = skin
def getBloodtype(self):
    return self.bloodtype
def getSkin(self):
    return self.skin            
    

birdOne = Birds("layeggs", "flying", "warmblooded", "feathers")
print(birdOne.reproduction)
print(birdOne.canmove)
print(birdOne.skin)












