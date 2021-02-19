class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.say_hello()

    def say_hello(self):
        print(self.name,self.age)


taro=Person('taro',20)
taro.name = "シマシマ"
taro.age = 18
taro.say_hello()




shimashima=Person('シマシマ',18)

print()

for i in range(2):
    shimashima.name=input()
    shimashima.age=input()
    shimashima.say_hello()
#taro.age=30
#taro.say_hello()
