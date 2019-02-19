class Building:
    lvl=0
    tipo=0 #1=HQ, 2=TC, 3=CP, 4=IM
    production=[0,0,0]
    population=0
    cost=[0,0,0,]

    def __init__(self,n):
        tipo=n
        
class Villaggio :
    
    hq=Building(1)
    tc=Building(2)
    cp=Building(3)
    
    def __init__(self):
        self.hq.lvl=1

    def build(self, obj):
        obj.lvl=obj.lvl+1

    def livello(self):
        return self.hq.lvl
    
mioVillo=Villaggio()
print("quartier generale %f" % mioVillo.livello())
mioVillo.build(mioVillo.hq)
print("quartier generale %f" % mioVillo.livello())

