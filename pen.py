from point import Point
from canvas import Canvas

class Pen (Point):
    def __init__(self, canvas:Canvas):
        super().__init__(0,0)
        self._canvas= canvas
        # tracks how many lines are made
        self._lines_drawn =0

    def move_to (self,point: Point):
        if isinstance(point, Point):
            self.x = point.x
            self.y = point.y

    def line_to (self,point1, point2):
        if isinstance (point1, Point) and isinstance(point2, Point):
            self._canvas.add_lines(point1, point2)

        # move pen to end point (destination)
        self.x = point2.x
        self.y = point2.y
        # update the line counter
        self._lines_drawn+=1

    def __str__(self):
        return f"pen at position ({self.x},{self.y})"

    def __repr__(self):
        return f"Pen(x={self.x}, y={self.y})"
    
    def reset(self):
        #Reset pen position to (0, 0) without drawing
        self.x = 0
        self.y = 0
    def __len__(self):
    #Return the number of lines drawn by the pen
        return self._lines_drawn


