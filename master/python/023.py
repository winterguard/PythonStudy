class Car():
    maxSpeed = 300
    maxPeople = 5
    def move(self, x):
        print(x, '의 스피드로 움직이고 있습니다.')
    def stop(self):
        print('멈췄습니다.')
k3 = Car()
k5 = Car()
print(k3.maxSpeed)
print(k5.maxPeople)
k3.move(5)
print(type(k3))
print(dir(k3))
print(k3)

