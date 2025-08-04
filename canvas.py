from point import Point
from line import Line

class Canvas:
    def __init__ (self, height, width, bg_color):
        self._lines=[]
        self.height = height
        self.width = width
        self.bg_color = bg_color

    def set (self, height= None, width= None, bg_color= None):
        if height is not None:
            self.height=height
        if width is not None:
            self.width=width
        if bg_color is not None:
            self.bg_color=bg_color
    
    def get(self):
        return f"height: {self.height}\n width: {self.width}\n background color:{self.bg_color}"

    def add_lines(self, p1:Point, p2:Point):
        line = Line (p1, p2)
        self._lines.append(line)

    def show(self):
        for line in self._lines:
            print(line)

    def __str__(self):
        return f"(width={self.width}, height={self.height}, bg_color='{self.bg_color}', lines={len(self._lines)})"


