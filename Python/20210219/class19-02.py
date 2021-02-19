import math
class Person:
    def __init__(self,name,x,y,z):
        self.name=name
        self.x=x
        self.y=y
        self.z=z
        

    def show_name(self):
        print(self.name+"合計: "+str(self.x+self.y+self.z)+", 平均: "+str(math.floor((self.x+self.y+self.z)/3)))

one=Person('シマシマ',39,70,10)
one.show_name()

two=Person('ヘンドリ',19,55,80)
two.show_name()

three=Person('ドル',55,72,96)
three.show_name()
