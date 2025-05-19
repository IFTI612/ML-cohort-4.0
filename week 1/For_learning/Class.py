class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self):
        print("Move")

    def Draw(self):
        print("Draw")    


#object = instance of a class

point = Point(10,20)
point.move()

print(point.x,point.y) #The use of constructor