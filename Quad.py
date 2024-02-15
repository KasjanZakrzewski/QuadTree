import random as Randy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Quad:
    def __init__(self, x1, x2, y1, y2, max):
        self.chidren = []
        self.points = []
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.max = max

    def split(self):
        quad = Quad(self.x1, (self.x1+self.x2)/2, self.y1, (self.y1+self.y2)/2, self.max)
        self.chidren.append(quad)

        quad = Quad((self.x1+self.x2)/2, self.x2, self.y1, (self.y1+self.y2)/2, self.max)
        self.chidren.append(quad)

        quad = Quad(self.x1, (self.x1+self.x2)/2, (self.y1+self.y2)/2, self.y2, self.max)
        self.chidren.append(quad)

        quad = Quad((self.x1+self.x2)/2, self.x2, (self.y1+self.y2)/2, self.y2, self.max)
        self.chidren.append(quad)

    def add_point(self, point):
        # spr czy mieści sie
        if (self.x1 <= point.x < self.x2) and (self.y1 <= point.y < self.y2):
            if len(self.points) == self.max:
                if len(self.chidren) == 0:
                    self.split()
                for child in self.chidren:
                    child.add_point(point)
            else:
                self.points.append(point)
    
    def intersect(self, x1, x2, y1, y2):
        return not (self.x2 < x1 or 
                    self.x1 > x2 or 
                    self.y1 > y2 or 
                    self.y2 < y1)

    def find_in_square(self, x1, x2, y1, y2):
        result = [] 
        if self.intersect(x1, x2, y1, y2):
            for point in self.points:
                if (x1 <= point.x < x2) and (y1 <= point.y < y2):
                    result.append(point)

            for child in self.chidren:
                result += child.find_in_square(x1, x2, y1, y2)      

        return result

tree = Quad(0, 64, 0, 64, 4)
all_points = []
find_points = []

for i in range(25):
    point = Point(Randy.randint(0,64),Randy.randint(0,64))
    all_points.append(point)
    tree.add_point(point)

find_points = tree.find_in_square(20, 30, 20, 30)

for point in all_points:
    print(point.x, "-", point.y)

print("=====")

for point in find_points:
    print(point.x, "-", point.y)

# for i in range(25):
#     point = Point(1,1)
#     tree.add_point(point)

None