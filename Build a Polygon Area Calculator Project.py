class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def set_width(self,width):
        self.width=width

    def set_height(self,height):
        self.height=height


    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2*self.width + 2*self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    def get_picture(self):
    # Check if the shape is too large to display
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
    
    # Build the picture as a string
        picture = ""
        for i in range(self.height):
            picture += '*' * self.width + '\n'
    
        return picture
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


    def get_amount_inside(self,shape):
        width_fit = self.width // shape.width
        height_fit = self.height // shape.height
        return width_fit * height_fit


class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side, side)
    
    def set_side(self,side):
        self.width = side
        self.height = side

    def set_width(self, width):
        # Override to keep the square property (all sides equal)
        self.set_side(width)

    def set_height(self, height):
        # Override to keep the square property (all sides equal)
        self.set_side(height)

    def __str__(self):
        # Return the string representation for Square
        return f"Square(side={self.width})"

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
