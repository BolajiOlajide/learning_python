class Rectangle:
    about = 'A rectangle is a 2 dimensional shape discussed in plane geometry'

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def get_area(self):
        return self.length * self.breadth

    def get_perimeter(self):
        return 2 * (self.length + self.breadth)

    def rect_name(self, name):
        return 'Your rectangle name is %s' % name

rect = Rectangle(10, 4)

print rect.get_area()
print rect.get_perimeter()
print rect.about
print rect.rect_name('Euclid')
