import sys
class BoundingRectangle:
    def init(self):
        self.minx = sys.maxsize
        self.maxx = -sys.maxsize
        self.miny = sys.maxsize
        self.maxy = -sys.maxsize

    def addpoint(self, x, y):
        self.minx = min(self.minx, x)
        self.maxx = max(self.maxx, x)
        self.miny = min(self.miny, y)
        self.maxy = max(self.maxy, y)

    def width(self):
        return self.maxx - self.minx
    def height(self):
        return self.maxy - self.miny
    def area(self):
        return self.width() * self.height()

rect = BoundingRectangle()
rect.addpoint(1, 1)
rect.addpoint(3, 3)
rect.addpoint(4, 1)
print(rect.width())
print(rect.height())
print(rect.area())

