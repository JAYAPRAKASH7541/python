class Rectangle:

    def __init__(self, length, breadth):
        # TODO: write your code here
        self.length=length
        self.breadth=breadth

    def get_area(self):
        # TODO: write your code here
        return self.length*self.breadth

    def get_perimeter(self):
        # TODO: write your code here
        return 2*(self.length+self.breadth)


if __name__ == "__main__":
    length = float(input())
    breadth = float(input())

    rectangle = Rectangle(length=length, breadth=breadth)
    print(rectangle.get_area())
    print(rectangle.get_perimeter())
