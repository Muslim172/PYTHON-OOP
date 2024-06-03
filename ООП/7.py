class BoundingRectangle(object):
    def __init__(self, points):
        self.points = points

    def add_point(self, point):
        self.points.append([point[0], point[1]])

    def width(self):
        x = [i[0] for i in self.points]
        return max(x) - min(x)

    def height(self):
        y = [i[1] for i in self.points]
        return max(y) - min(y)

    def bottom_y(self):
        return min([i[1] for i in self.points])

    def top_y(self):
        return max([i[1] for i in self.points])

    def left_x(self):
        return min([i[0] for i in self.points])

    def right_x(self):
        return max([i[0] for i in self.points])


p = [[0, 0]]
a = BoundingRectangle(p)
print(a.width(), a.height(), a.bottom_y(), a.left_x(), a.right_x(), a.top_y())
a.add_point([1, 1])
print(a.width(), a.height(), a.bottom_y(), a.left_x(), a.right_x(), a.top_y())


# Ваш код

rect = BoundingRectangle()
rect.add_point(-1, -2)
rect.add_point(3, 4)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())