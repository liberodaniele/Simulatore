class Building:
    lvl=0
    tipo=0 #1=HQ, 2=TC, 3=CP, 4=IM
    production=[0,0,0]
    population=0
    cost=[0,0,0]
    time=0

    def __init__(self,n):
        tipo=n

    def upgrade(self):
        self.lvl=self.lvl+1
        
class Villaggio :

    resources=[100,1,1]
    population=0
    hq=Building(1)
    tc=Building(2)
    cp=Building(3)
    
    def __init__(self):
        self.hq.lvl=0

    def build(self, obj):
        if obj.cost[0]<self.resources[0] & obj.cost[1]<self.resources[1] & obj.cost[2]<self.resources[2]:
            obj.upgrade()

    def livello(self):
        return self.hq.lvl
    
mioVillo=Villaggio()
print("quartier generale %f" % mioVillo.livello())
mioVillo.build(mioVillo.hq)
print("quartier generale %f" % mioVillo.livello())

