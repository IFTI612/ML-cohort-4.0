class Rec:
    def __init__(self, l , b):
        self.l = l
        self.b = b

    def area(self):
        a = self.l*self.b
        print(f"The Area is {a}")   

len = float(input("Enter Length___"))
bre = float(input("Enter Breadth__"))
rec =Rec(len , bre)
rec.area()