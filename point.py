class Point:
    def __init__(self, x, y):
        self._x = x 
        self._y = y

    # === Property for x ===
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    # === Property for y ===
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    # === Set Method ===
    def set(self, x=None, y=None):
        if x is not None:
            self.x = x  
        if y is not None:
            self.y = y

    # === Get Method ===
    def get(self):
        return (self.x, self.y)

    # === Copy Constructor ===
    @classmethod
    def copy(cls, otherPoint):
        return cls(otherPoint.x, otherPoint.y)

    # === String Representation ===
    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"

    # === Operator Overload (+) ===
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
        

    # === Show Method ===
    def show(self):
        print(self.__str__())
