from point import Point
class Circle:
    def __init__(self, center: Point, radius):
        self.center = center
        self._radius = radius

    @property
    def radius (self):
        return self._radius
    @radius.setter
    def radius (self,new_radius):
        if new_radius <=0:
            print("invalid radius")
            return
        self._radius = new_radius

    def set(self, new_cp= None,new_radius= None ):
        if new_cp is not None:
            self.center = new_cp
        if new_radius is not None:
            self.radius = new_radius

    def get_cp (self):
        return f"center point: {self.center}\n Radius: {self.radius}"
    
    def area(self):
        return 3.142* self.radius **2

    def circumference(self):
        return 2* 3.142*self.radius
    
    def __str__(self):
        return f"center point: {self.center}\n Radius: {self.radius}\n Area: {self.area()}\n Circumference {self.circumference()}"


    def show(self):
        print(f"a circle having center point at {self.center} and radius of {self.radius}")




    
